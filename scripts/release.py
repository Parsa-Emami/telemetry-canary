import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def main():
    tag = sys.argv[1]
    if not re.fullmatch(r"v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", tag):
        raise SystemExit("expected a vMAJOR.MINOR.PATCH tag")
    name = "telemetry-canary"
    target = Path("dist")
    target.mkdir(exist_ok=True)
    archive = target / f"{name}-{tag}.tar.gz"
    subprocess.run(["git", "archive", "--format=tar.gz", f"--prefix={name}-{tag}/",
                    f"--output={archive}", "HEAD"], check=True)
    component = {
        "type": "application",
        "bom-ref": name,
        "name": name,
        "version": tag[1:],
        "licenses": [{"license": {"id": "Apache-2.0"}}],
    }
    bom = {"bomFormat": "CycloneDX", "specVersion": "1.6", "version": 1,
           "metadata": {"component": component}, "components": [],
           "dependencies": [{"ref": name, "dependsOn": []}]}
    sbom = target / "sbom.cdx.json"
    sbom.write_text(json.dumps(bom, indent=2) + "\n", encoding="utf-8")
    with (target / "SHA256SUMS").open("w", encoding="ascii") as checksums:
        for artifact in (archive, sbom):
            with artifact.open("rb") as stream:
                digest = hashlib.file_digest(stream, "sha256").hexdigest()
            checksums.write(f"{digest}  {artifact.name}\n")
    if output_path := os.environ.get("GITHUB_OUTPUT"):
        with Path(output_path).open("a", encoding="utf-8") as output:
            print(f"archive={archive.as_posix()}", file=output)


if __name__ == "__main__":
    main()
