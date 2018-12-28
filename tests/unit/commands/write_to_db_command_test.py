import unittest
from unittest.mock import MagicMock

from sqlalchemy.exc import SQLAlchemyError

from commands.write_to_db_command import WriteToDbCommand
from models.services.db_service import DBService
from models.db.session_maker import SessionMaker
from models.db.user import User


class WriteToDbCommandTest(unittest.TestCase):
    def setUp(self):
        session = SessionMaker.make_session(True)
        user = User()
        db_service = DBService(session, user)
        self.command = WriteToDbCommand(db_service)

    def tearDown(self):
        pass

    def test_execute(self):
        self.command.db_service.save = MagicMock(return_value=True)
        self.assertTrue(self.command.execute())

    def test_failed_execute(self):
        with self.assertRaises(SQLAlchemyError):
            self.assertFalse(self.command.execute())

    def test_undo(self):
        self.command.db_service.delete = MagicMock(return_value=True)
        self.command.undo()

    def test_failed_undo(self):
        with self.assertRaises(SQLAlchemyError):
            self.command.undo()
