import unittest
import os

from sqlalchemy.orm.session import Session

from models.db import SessionMaker, EngineMaker


class SessionMakerTest(unittest.TestCase):
    def setUp(self):
        self.os_dict_keys = ['DB_LOGIN', 'DB_PASSWORD', 'DB_HOST', 'DB_DB']
        for key in self.os_dict_keys:
            os.environ[key] = 'test_var'

    def tearDown(self):
        for key in self.os_dict_keys:
            os.environ.pop(key)

    def test_session_init(self):
        engine = EngineMaker.make_engine()
        session = SessionMaker.make_session(engine)
        self.assertIsInstance(session, Session)
