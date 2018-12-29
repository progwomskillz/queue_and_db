import unittest
from unittest.mock import MagicMock

from commands import SendEmailCommand


class SendEmailCommandTest(unittest.TestCase):
    def setUp(self):
        self.email_service = MagicMock()
        self.command = SendEmailCommand(self.email_service)

    def tearDown(self):
        pass

    def test_execute(self):
        self.assertFalse(self.command.execute())
        self.email_service.send.assert_called_once()
