"""Post the Jenkins build result to Webex. Standard library only."""
import argparse
import json
import os
import sys
import urllib.request

WEBEX_URL = "https://webexapis.com/v1/messages"


def build_message(status, build_number, commit, branch="main"):
    """Return the markdown posted to the Webex space."""
    short = (commit or "unknown")[:7]
    if status == "SUCCESS":
        head = f"**DEPLOYED** · Outage Watch build #{build_number} · {branch} @ {short}"
        body = "All unit tests passed. The new version is live."
    else:
        head = f"**BUILD FAILED** · Outage Watch build #{build_number} · {branch} @ {short}"
        body = "Tests or deploy failed. Nothing was deployed. Check Jenkins."
    return f"{head}\n\n{body}"


def post(token, room_id, markdown, opener=urllib.request.urlopen):
    """Send one markdown message to a Webex room. Returns the HTTP status."""
    payload = json.dumps({"roomId": room_id, "markdown": markdown}).encode()
    request = urllib.request.Request(
        WEBEX_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with opener(request, timeout=10) as response:
        return response.status


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--status", choices=["SUCCESS", "FAILURE"], required=True)
    args = parser.parse_args(argv)
    message = build_message(
        args.status,
        os.environ.get("BUILD_NUMBER", "?"),
        os.environ.get("GIT_COMMIT", ""),
        os.environ.get("BRANCH_NAME", "main"),
    )
    token = os.environ.get("WEBEX_TOKEN")
    room_id = os.environ.get("WEBEX_ROOM_ID")
    if not token or not room_id:
        print("WEBEX_TOKEN or WEBEX_ROOM_ID not set; message not sent:")
        print(message)
        return 0
    post(token, room_id, message)
    print("Posted to Webex.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
