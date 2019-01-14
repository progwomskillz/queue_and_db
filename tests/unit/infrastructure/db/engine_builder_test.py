import unittest
from unittest.mock import MagicMock

import sqlalchemy.engine

from infrastructure.db import EngineBuilder


class EngineBuilderTest(unittest.TestCase):
    def setUp(self):
        self.environment_manager = MagicMock()
        self.environment_manager.get_var_from_env = MagicMock(
            return_value='Test'
        )
        self.engine_builder = EngineBuilder(self.environment_manager)

    def tearDown(self):
        pass

    def test_build(self):
        engine = self.engine_builder.build()
        self.assertIsInstance(engine, sqlalchemy.engine.Engine)
        keys = ['DB_LOGIN', 'DB_PASSWORD', 'DB_HOST', 'DB_DB']
        for key in keys:
            self.environment_manager.get_var_from_env.assert_any_call(key)
