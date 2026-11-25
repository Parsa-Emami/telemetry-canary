import argparse
import json
from pathlib import Path

from engine import evaluate


def unique_object(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate field")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description="Check exported logs and traces for synthetic privacy canaries.")
    parser.add_argument("fixture", type=Path)
    options = parser.parse_args()
    try:
        if options.fixture.stat().st_size > 2 * 1024 * 1024:
            raise ValueError("fixture exceeds size limit")
        data = json.loads(options.fixture.read_text(encoding="utf-8"),
                          object_pairs_hook=unique_object)
        if not isinstance(data, dict):
            raise ValueError("fixture must be a JSON object")
        findings = evaluate(data, options.fixture)
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError):
        print(json.dumps({"status": "invalid_input", "findings": []}))
        return 2
    status = "findings" if findings else "ok"
    print(json.dumps({"status": status, "findings": findings}, sort_keys=True))
    return int(bool(findings))


if __name__ == "__main__":
    raise SystemExit(main())
