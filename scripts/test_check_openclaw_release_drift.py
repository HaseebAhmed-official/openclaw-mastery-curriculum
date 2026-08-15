import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_openclaw_release_drift import build_issue_body, build_release_request


class ReleaseRequestTests(unittest.TestCase):
    def test_request_uses_token_without_exposing_it_in_url(self):
        with patch.dict("os.environ", {"GH_TOKEN": "secret-token"}, clear=True):
            request = build_release_request("owner/repo")

        self.assertEqual("Bearer secret-token", request.headers["Authorization"])
        self.assertNotIn("secret-token", request.full_url)

    def test_request_can_run_unauthenticated(self):
        with patch.dict("os.environ", {}, clear=True):
            request = build_release_request("owner/repo")

        self.assertNotIn("Authorization", request.headers)


class IssueBodyTests(unittest.TestCase):
    def test_issue_body_reports_baseline_latest_and_surfaces(self):
        state = {
            "tracked_repo": "owner/repo",
            "last_reviewed_release": "v1",
            "last_reviewed_date": "2026-01-01",
            "review_surfaces": ["curriculum/case-studies.md"],
        }
        latest = {
            "tag_name": "v2",
            "html_url": "https://example.invalid/v2",
            "published_at": "2026-01-02T00:00:00Z",
        }

        body = build_issue_body(state, latest)

        self.assertIn("v1", body)
        self.assertIn("v2", body)
        self.assertIn("curriculum/case-studies.md", body)

    def test_issue_body_reports_healthy_equal_baseline(self):
        state = {
            "tracked_repo": "owner/repo",
            "last_reviewed_release": "v2",
            "last_reviewed_date": "2026-01-01",
        }
        latest = {
            "tag_name": "v2",
            "html_url": "https://example.invalid/v2",
            "published_at": "2026-01-02T00:00:00Z",
        }

        body = build_issue_body(state, latest)

        self.assertIn("baseline current", body)
        self.assertIn("No release-drift review issue is required", body)
        self.assertNotIn("upstream review required", body)


if __name__ == "__main__":
    unittest.main()
