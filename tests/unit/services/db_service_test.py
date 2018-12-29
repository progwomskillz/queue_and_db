import unittest
from unittest.mock import MagicMock
import os

from models.services import DBService
from models.db import SessionMaker, EngineMaker, User


class DBServiceTest(unittest.TestCase):
    def setUp(self):
        self.os_dict_keys = ['DB_LOGIN', 'DB_PASSWORD', 'DB_HOST', 'DB_DB']
        for key in self.os_dict_keys:
            os.environ[key] = 'test_var'

        engine = EngineMaker.make_engine()
        session = SessionMaker.make_session(engine)
        session.commit = MagicMock(return_value=True)
        user = User(id=1, first_name='Nik', last_name='S.')
        self.db = DBService(session, user)

    def tearDown(self):
        for key in self.os_dict_keys:
            os.environ.pop(key)

    def test_save(self):
        self.db.save()

    def test_delete(self):
        self.db.session.delete = MagicMock(return_value=True)
        self.db.delete()
