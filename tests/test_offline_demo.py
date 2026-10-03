"""Verify the public demo remains offline and side-effect free."""

import contextlib
import io
from pathlib import Path
import unittest
from unittest.mock import patch

from xuewuzhi_downloader.cli import main


class OfflineContractTests(unittest.TestCase):
    def test_demo_cannot_open_a_network_connection(self):
        out = io.StringIO()
        with patch("socket.socket", side_effect=AssertionError("network forbidden")):
            with patch.object(Path, "write_text", side_effect=AssertionError("write forbidden")):
                with patch.object(Path, "write_bytes", side_effect=AssertionError("write forbidden")):
                    with contextlib.redirect_stdout(out):
                        self.assertEqual(main(["demo"]), 0)
        self.assertIn("未下载文件", out.getvalue())
        self.assertIn("练习讲义.pdf", out.getvalue())

    def test_catalog_search_is_offline_and_explains_implementation_scope(self):
        out = io.StringIO()
        with patch("socket.socket", side_effect=AssertionError("network forbidden")):
            with contextlib.redirect_stdout(out):
                self.assertEqual(main(["platforms", "--query", "MOOC"]), 0)
        self.assertIn("MOOC", out.getvalue())
        self.assertIn("适配器未包含", out.getvalue())

    def test_no_match_is_reported_without_falling_back_to_a_service(self):
        out = io.StringIO()
        with patch("socket.socket", side_effect=AssertionError("network forbidden")):
            with contextlib.redirect_stdout(out):
                self.assertEqual(main(["platforms", "--query", "__unknown_platform__"]), 0)
        self.assertIn("共 0 个结果", out.getvalue())


if __name__ == "__main__":
    unittest.main()
