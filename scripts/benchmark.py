import json
import platform
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine import evaluate


def main():
    fixture = ROOT / "examples" / "finding.json"
    data = json.loads(fixture.read_text(encoding="utf-8"))
    timings = []
    for _ in range(101):
        start = time.perf_counter_ns()
        evaluate(data, fixture)
        timings.append(time.perf_counter_ns() - start)
    print(json.dumps({"iterations": 100, "median_ns": statistics.median(timings[1:]),
                      "python": platform.python_version(), "platform": platform.platform()}))


if __name__ == "__main__":
    main()
