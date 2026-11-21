"""TC-06: the Webex announcement, without touching the network."""
import json
import unittest
from unittest import mock

from ci import announce


class AnnounceTests(unittest.TestCase):
    def test_success_message_names_build_and_status(self):
        msg = announce.build_message("SUCCESS", "19", "4f9c2e1abc")
        self.assertIn("DEPLOYED", msg)
        self.assertIn("#19", msg)
        self.assertIn("4f9c2e1", msg)

    def test_failure_message_says_failed(self):
        msg = announce.build_message("FAILURE", "20", "abc1234")
        self.assertIn("BUILD FAILED", msg)
        self.assertIn("Nothing was deployed", msg)

    def test_post_sends_token_in_header_not_body(self):
        response = mock.MagicMock(status=200)
        response.__enter__.return_value = response
        opener = mock.Mock(return_value=response)
        announce.post("secret-token", "room-1", "hello", opener=opener)
        request = opener.call_args[0][0]
        self.assertEqual(request.get_header("Authorization"), "Bearer secret-token")
        body = json.loads(request.data)
        self.assertEqual(body, {"roomId": "room-1", "markdown": "hello"})

    @mock.patch.dict("os.environ", {"BUILD_NUMBER": "7"}, clear=True)
    def test_missing_token_does_not_fail_the_build(self):
        self.assertEqual(announce.main(["--status", "SUCCESS"]), 0)


if __name__ == "__main__":
    unittest.main()
