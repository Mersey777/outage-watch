"""TC-01 to TC-05: status_check.py, offline with fixtures and mocks."""
import json
import unittest
from pathlib import Path
from unittest import mock

import requests

import status_check

FIXTURES = Path(__file__).parent / "fixtures"


def load(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class SummarizeTests(unittest.TestCase):
    def test_tc01_all_green(self):
        indicator, description, problems = status_check.summarize(load("all_green.json"))
        self.assertEqual(indicator, "none")
        self.assertEqual(description, "All Systems Operational")
        self.assertEqual(problems, [])

    def test_tc02_degraded(self):
        indicator, _, problems = status_check.summarize(load("degraded.json"))
        self.assertEqual(indicator, "minor")
        self.assertEqual(problems, [("Actions", "degraded_performance")])

    def test_tc03_outage(self):
        indicator, _, problems = status_check.summarize(load("outage.json"))
        self.assertEqual(indicator, "major")
        self.assertIn(("Git Operations", "major_outage"), problems)
        self.assertIn(("Webhooks", "partial_outage"), problems)
        self.assertEqual(len(problems), 2)

    def test_report_lists_each_problem(self):
        report = status_check.format_report(*status_check.summarize(load("outage.json")))
        self.assertIn("Git Operations: major_outage", report)

    def test_tc07_report_counts_affected_components(self):
        report = status_check.format_report(*status_check.summarize(load("outage.json")))
        self.assertIn("2 affected", report.splitlines()[0])


class FetchTests(unittest.TestCase):
    @mock.patch("status_check.requests.get", side_effect=requests.Timeout)
    def test_tc04_timeout_gives_clear_message(self, _get):
        with self.assertRaises(status_check.StatusError) as ctx:
            status_check.fetch_summary(timeout=5)
        self.assertIn("timed out", str(ctx.exception))

    @mock.patch("status_check.requests.get")
    def test_tc05_server_error_names_status(self, get):
        get.return_value = mock.Mock(status_code=500)
        with self.assertRaises(status_check.StatusError) as ctx:
            status_check.fetch_summary()
        self.assertIn("HTTP 500", str(ctx.exception))

    @mock.patch("status_check.fetch_summary", side_effect=status_check.StatusError("x"))
    def test_main_returns_1_on_error(self, _fetch):
        self.assertEqual(status_check.main(), 1)


if __name__ == "__main__":
    unittest.main()
