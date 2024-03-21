"""testing module for the parser"""

import unittest
import expectenv


class EnvTest(unittest.TestCase):
    """test class"""

    def test_keys(self):
        """testing key list generation"""
        parser = expectenv.Parser("testing")
        parser.bind("db_host")
        keys = parser.keys()
        self.assertListEqual(keys, ["db_host"])

    def test_bind_with_env(self):
        """testing default use case"""
        parser = expectenv.Parser("testing")
        # should be in env
        parser.bind("db_host")
        try:
            parser.parse()
        except expectenv.EnvError as ee:
            self.assertIsNone(ee)

    def test_bind_with_optional_env(self):
        """test binding optional var with empty"""
        parser = expectenv.Parser("shenanigans")
        # should not be in env
        parser.bind("db_host", optional=True)
        try:
            parser.parse()
        except expectenv.EnvError as ee:
            self.assertIsNone(ee)

    def test_get_configs(self):
        """test get config dict"""
        parser = expectenv.Parser("testing")
        parser.bind("db_host")
        try:
            parser.parse()
        except expectenv.EnvError as ee:
            self.assertIsNone(ee)
        confs = parser.configs()
        # This assumes an `export TESTING_DB_HOST=localhost` was run in the env
        self.assertDictEqual(confs, {"db_host": "localhost"})
