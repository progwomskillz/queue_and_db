import unittest
import os

import sqlalchemy.engine

from models.db import EngineMaker
from exceptions.environment import VariableCantBeImport


class EngineMakerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_engine_init(self):
        os_dict_keys = ['DB_LOGIN', 'DB_PASSWORD', 'DB_HOST', 'DB_DB']
        for key in os_dict_keys:
            os.environ[key] = 'test_var'

        engine = EngineMaker.make_engine()
        self.assertIsInstance(engine, sqlalchemy.engine.Engine)

        for key in os_dict_keys:
            os.environ.pop(key)

    def test_failed_engine_init(self):
        with self.assertRaises(VariableCantBeImport):
            EngineMaker.make_engine()
