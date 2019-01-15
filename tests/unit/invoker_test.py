import unittest
from unittest.mock import MagicMock

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
        self.assertTrue(self.invoker.execute_commands())
        for command in self.invoker.commands:
            command.execute.assert_called_once()

    def test_execute_commands_with_error(self):
        self.invoker.commands[0].execute = MagicMock(
            side_effect=CommandRuntimeError('Test error')
        )
        self.assertFalse(self.invoker.execute_commands())
        for command in self.invoker.command_history:
            command.undo.assert_called_once()
