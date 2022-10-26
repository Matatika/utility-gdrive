"""Unittest module for utility-gdrive"""

import unittest
from click.testing import CliRunner
from utility_gdrive.cli.commands.root import root


class TestGDriveUtility(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.file_id = "file12345"
        self.folder_id = "folder12345"

    def tearDown(self):
        pass

    def test_convert_no_file_path(self):
        result = self.runner.invoke(root, catch_exceptions=False)
        self.assertIn("Error", result.output)
        self.assertIs(result.exit_code, 2)
