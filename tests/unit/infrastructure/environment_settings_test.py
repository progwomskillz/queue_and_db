import unittest
import os

from models.environment_settings import EnvironmentSettings
from exceptions.environment import VariableCantBeImport


class EnvironmentSettingsTest(unittest.TestCase):
    def setUp(self):
        self.key = 'TEST_VARIABLE'
        self.value = 'TEST_STRING'

    def tearDown(self):
        pass

    def test_get_available_var(self):
        os.environ[self.key] = self.value
        value = EnvironmentSettings.get_var_from_env(self.key)
        self.assertEqual(value, self.value)
        os.environ.pop(self.key)

    def test_get_unavailable_var(self):
        with self.assertRaises(VariableCantBeImport):
            EnvironmentSettings.get_var_from_env(self.key)
