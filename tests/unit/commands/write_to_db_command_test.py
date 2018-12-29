import unittest
from unittest.mock import MagicMock

from commands import WriteToDbCommand


class WriteToDbCommandTest(unittest.TestCase):
    def setUp(self):
        self.db_service = MagicMock()
        self.command = WriteToDbCommand(self.db_service)

    def tearDown(self):
        pass

    def test_execute(self):
        self.assertTrue(self.command.execute())
        self.db_service.save.assert_called_once()

    def test_undo(self):
        self.command.undo()
        self.db_service.delete.assert_called_once()
