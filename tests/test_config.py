"""Tests for the backend configuration system.

Uses Python's built-in ``unittest`` module only (no external libraries).
"""

import unittest

from backend.config import Config


class TestConfig(unittest.TestCase):
    """Basic tests for the Config class."""

    def test_config_can_be_created(self):
        """A Config object can be instantiated."""
        config = Config()
        self.assertIsInstance(config, Config)

    def test_project_name_has_default(self):
        """PROJECT_NAME is present and non-empty by default."""
        config = Config()
        self.assertIsInstance(config.PROJECT_NAME, str)
        self.assertTrue(config.PROJECT_NAME)

    def test_environment_has_default(self):
        """ENVIRONMENT is present and non-empty by default."""
        config = Config()
        self.assertIsInstance(config.ENVIRONMENT, str)
        self.assertTrue(config.ENVIRONMENT)


if __name__ == "__main__":
    unittest.main()
