import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from engine import evaluate

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples"


def cli(fixture):
    return subprocess.run([sys.executable, str(ROOT / "check.py"), str(fixture)],
                          capture_output=True, text=True, timeout=10, check=False)


class EngineTests(unittest.TestCase):
    def test_pass_fixture(self):
        fixture = FIXTURES / "pass.json"
        self.assertEqual(evaluate(json.loads(fixture.read_text()), fixture), [])

    def test_finding_fixture(self):
        fixture = FIXTURES / "finding.json"
        codes = {item["code"] for item in evaluate(json.loads(fixture.read_text()), fixture)}
        self.assertIn("synthetic_canary_observed", codes)


class CliTests(unittest.TestCase):
    def test_reports_pass(self):
        result = cli(FIXTURES / "pass.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"status": "ok", "findings": []})

    def test_reports_findings(self):
        result = cli(FIXTURES / "finding.json")
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["status"], "findings")
        self.assertIn("synthetic_canary_observed", {item["code"] for item in report["findings"]})
        self.assertNotIn("tc-test-001", result.stdout)

    def test_rejects_invalid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "invalid.json"
            fixture.write_text('{"duplicate": 1, "duplicate": 2}')
            result = cli(fixture)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"status": "invalid_input", "findings": []})
