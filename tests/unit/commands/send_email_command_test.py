import unittest
from unittest.mock import MagicMock

from requests.exceptions import RequestException

from commands import SendEmailCommand
from infrastructure.exceptions import CommandRuntimeError


class SendEmailCommandTest(unittest.TestCase):
    def setUp(self):
        self.email_service = MagicMock()
        self.command = SendEmailCommand(self.email_service)

    def tearDown(self):
        pass

    def test_execute(self):
        self.assertFalse(self.command.execute())
        self.email_service.send.assert_called_once()

    def test_execute_with_error(self):
        self.command.email_service.send = MagicMock(
            side_effect=RequestException('Test error')
        )
        with self.assertRaises(CommandRuntimeError):
            self.command.execute()
            self.email_service.send.assert_called_once()
