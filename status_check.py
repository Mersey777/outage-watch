"""Outage Watch v0: print GitHub's current status from its public Statuspage API."""
import sys

import requests

SUMMARY_URL = "https://www.githubstatus.com/api/v2/summary.json"
NON_OPERATIONAL = (
    "degraded_performance",
    "partial_outage",
    "major_outage",
    "under_maintenance",
)


class StatusError(Exception):
    """Raised when the status API can't be read."""


def fetch_summary(url=SUMMARY_URL, timeout=5):
    """Return the parsed summary.json, or raise StatusError with a clear message."""
    try:
        response = requests.get(url, timeout=timeout)
    except requests.Timeout:
        raise StatusError(f"GitHub status timed out after {timeout} s") from None
    except requests.RequestException as err:
        raise StatusError(f"GitHub status unreachable: {err}") from None
    if response.status_code != 200:
        raise StatusError(f"GitHub status returned HTTP {response.status_code}")
    return response.json()


def summarize(data):
    """Return (indicator, description, problems) from a summary.json dict."""
    status = data.get("status", {})
    problems = [
        (c["name"], c["status"])
        for c in data.get("components", [])
        if c.get("status") in NON_OPERATIONAL
    ]
    return status.get("indicator", "unknown"), status.get("description", ""), problems


def format_report(indicator, description, problems):
    """Return the text printed to the L1 shift."""
    lines = [f"GitHub status: {description} (indicator: {indicator}), {len(problems)} affected"]
    for name, state in problems:
        lines.append(f"  - {name}: {state}")
    return "\n".join(lines)


def main():
    try:
        data = fetch_summary()
    except StatusError as err:
        print(err)
        return 1
    print(format_report(*summarize(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
