import unittest
from unittest.mock import MagicMock

from sqlalchemy.exc import SQLAlchemyError

from commands import WriteToDbCommand
from infrastructure.exceptions import CommandRuntimeError


class WriteToDbCommandTest(unittest.TestCase):
    def setUp(self):
        self.db_service = MagicMock()
        self.command = WriteToDbCommand(self.db_service)

    def tearDown(self):
        pass

    def test_execute(self):
        self.assertTrue(self.command.execute())
        self.db_service.save.assert_called_once()

    def test_execute_with_error(self):
        self.command.db_service.save = MagicMock(
            side_effect=SQLAlchemyError('Test error')
        )
        with self.assertRaises(CommandRuntimeError):
            self.command.execute()
            self.db_service.save.assert_called_once()

    def test_undo(self):
        self.command.undo()
        self.db_service.delete.assert_called_once()

    def test_undo_with_error(self):
        self.command.db_service.delete = MagicMock(
            side_effect=SQLAlchemyError('Test error')
        )
        with self.assertRaises(CommandRuntimeError):
            self.command.undo()
            self.db_service.delete.assert_called_once()
