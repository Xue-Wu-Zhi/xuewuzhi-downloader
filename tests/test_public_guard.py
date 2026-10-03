from pathlib import Path
import unittest

from scripts.check_public_tree import inspect_file


class PublicGuardTests(unittest.TestCase):
    def test_rejects_private_key_nested_under_docs(self):
        secret = ("-----BEGIN " + "PRIVATE KEY-----\nexample").encode()
        self.assertTrue(inspect_file(Path("docs/notes.md"), secret))

    def test_rejects_token_inside_otherwise_valid_python_file(self):
        token = ("example = 'gh" + "p_" + "x" * 36 + "'").encode()
        self.assertTrue(inspect_file(Path("xuewuzhi_downloader/example.py"), token))

    def test_rejects_installers_in_source_tree(self):
        self.assertTrue(inspect_file(Path("assets/client.exe"), b"MZ"))

    def test_rejects_unreviewed_top_level_folder(self):
        self.assertTrue(inspect_file(Path("private/source.py"), b"print('hello')"))

    def test_accepts_public_documentation(self):
        self.assertEqual(inspect_file(Path("docs/example.md"), b"# Public guide\n"), [])


if __name__ == "__main__":
    unittest.main()
