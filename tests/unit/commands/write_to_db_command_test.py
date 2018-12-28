import unittest
from unittest.mock import MagicMock
import os

from sqlalchemy.exc import SQLAlchemyError

from commands.write_to_db_command import WriteToDbCommand
from models.services.db_service import DBService
from models.db.session_maker import SessionMaker
from models.db.engine_maker import EngineMaker
from models.db.user import User


class WriteToDbCommandTest(unittest.TestCase):
    def setUp(self):
        self.os_dict_keys = ['DB_LOGIN', 'DB_PASSWORD', 'DB_HOST', 'DB_DB']
        for key in self.os_dict_keys:
            os.environ[key] = 'test_var'

        engine = EngineMaker.make_engine()
        session = SessionMaker.make_session(engine)
        user = User(id=1, first_name='Nik', last_name='S.')
        db_service = DBService(session, user)
        self.command = WriteToDbCommand(db_service)

    def tearDown(self):
        for key in self.os_dict_keys:
            os.environ.pop(key)

    def test_execute(self):
        self.command.db_service.save = MagicMock(return_value=True)
        self.assertTrue(self.command.execute())

    def test_failed_execute(self):
        with self.assertRaises(SQLAlchemyError):
            self.assertTrue(self.command.execute())

    def test_undo(self):
        self.command.db_service.delete = MagicMock(return_value=True)
        self.command.undo()

    def test_failed_undo(self):
        with self.assertRaises(SQLAlchemyError):
            self.command.undo()
