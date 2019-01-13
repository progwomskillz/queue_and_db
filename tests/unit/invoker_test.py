import unittest
from unittest.mock import MagicMock

from requests.exceptions import RequestException
from sqlalchemy.exc import SQLAlchemyError

from invoker import Invoker
from infrastructure.exceptions import CommandRuntimeError


class InvokerTest(unittest.TestCase):
    def setUp(self):
        db_command = MagicMock()
        email_command = MagicMock()

        commands = [db_command, email_command]
        self.invoker = Invoker(commands)

    def tearDown(self):
        pass

    def test_execute_commands(self):
        self.invoker.execute_commands()
        for command in self.invoker.commands:
            command.execute.assert_called_once()

    def test_execute_command_with_request_error(self):
        self.invoker.commands[1].execute = MagicMock(
            side_effect=RequestException()
        )

        with self.assertRaises(CommandRuntimeError):
            with self.assertRaises(RequestException):
                self.invoker.execute_commands()

                for command in self.invoker.commands:
                    command.execute.assert_called_once()

                for command in self.invoker.command_history:
                    command.undo.assert_called_once()

    def test_execute_command_with_sql_error(self):
        self.invoker.commands[0].execute = MagicMock(
            side_effect=SQLAlchemyError()
        )

        with self.assertRaises(CommandRuntimeError):
            with self.assertRaises(SQLAlchemyError):
                self.invoker.execute_commands()

                for command in self.invoker.commands:
                    command.execute.assert_called_once()

                for command in self.invoker.command_history:
                    command.undo.assert_called_once()
