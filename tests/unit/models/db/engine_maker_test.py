import unittest
import os

from sqlalchemy.engine import Engine

from models.db.engine_maker import EngineMaker
from exceptions.environment.variable_cant_be_import import VariableCantBeImport


class EngineMakerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_engine_init(self):
        os.environ['DB_LOGIN'] = 'test'
        os.environ['DB_PASSWORD'] = 'test'
        os.environ['DB_HOST'] = 'test'
        os.environ['DB_DB'] = 'test'
        engine = EngineMaker.make_engine()
        self.assertIsInstance(engine, Engine)
        os.environ.pop('DB_LOGIN')
        os.environ.pop('DB_PASSWORD')
        os.environ.pop('DB_HOST')
        os.environ.pop('DB_DB')

    def test_failed_engine_init(self):
        with self.assertRaises(VariableCantBeImport):
            EngineMaker.make_engine()
