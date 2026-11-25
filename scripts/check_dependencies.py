import ast
import re
import subprocess
import sys
from pathlib import Path

DEPENDENCY_MANIFESTS = re.compile(
    r"(?i)(pyproject\.toml|setup\.(py|cfg)|requirements.*\.(txt|in)|Pipfile(\.lock)?|"
    r"poetry\.lock|uv\.lock|pdm\.lock|package(-lock)?\.json|yarn\.lock|pnpm-lock\.yaml|"
    r"go\.(mod|sum)|pom\.xml|Cargo\.(toml|lock)|Gemfile(\.lock)?|build\.gradle(\.kts)?|"
    r"gradle\.lockfile|composer\.(json|lock)|Dockerfile.*|Containerfile.*|.*\.whl)"
)
PINNED_ACTION = re.compile(r"^\s*(?:-\s*)?uses:\s+[-\w.]+/[-\w./]+@[0-9a-f]{40}\s*$")


def tracked_files():
    result = subprocess.run(["git", "ls-files", "-z"], check=True, capture_output=True, text=True)
    return [Path(name) for name in result.stdout.split("\0") if name]


def main():
    paths = tracked_files()
    first_party = {path.stem for path in paths if len(path.parts) == 1 and path.suffix == ".py"}
    allowed = sys.stdlib_module_names | first_party
    errors = []
    for path in paths:
        if DEPENDENCY_MANIFESTS.fullmatch(path.name):
            errors.append(f"{path}: review the dependency and add lockfile-based advisory scanning")
        if path.suffix == ".py":
            for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"), filename=str(path))):
                if isinstance(node, ast.Import):
                    names = [alias.name for alias in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0:
                    names = [node.module]
                else:
                    continue
                for name in names:
                    if name and name.partition(".")[0] not in allowed:
                        errors.append(f"{path}:{node.lineno}: unreviewed dependency {name}")
        if path.parent.as_posix() == ".github/workflows":
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if re.match(r"^\s*(?:-\s*)?uses\s*:", line) and not PINNED_ACTION.fullmatch(line):
                    errors.append(f"{path}:{number}: an action must be pinned to a full commit SHA")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("No third-party runtime dependencies. Workflow action references are commit-pinned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
