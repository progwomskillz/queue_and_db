import unittest
from unittest.mock import MagicMock
import os

from requests.exceptions import RequestException

from commands.send_email_command import SendEmailCommand
from models.services.email_service import EmailService
from exceptions.commands.command_cant_be_undone import CommandCantBeUndone


class SendEmailCommandTest(unittest.TestCase):
    def setUp(self):
        self.os_dict_keys = ['EMAIL_URL', 'EMAIL_TOKEN']
        for key in self.os_dict_keys:
            os.environ[key] = 'test_var'
        message = {
            'from': 'Man <man@example.com>',
            'to': 'admin@example.com',
            'subject': 'Success',
            'text': 'Write successfully!'
        }
        email_service = EmailService(message)
        self.command = SendEmailCommand(email_service)

    def tearDown(self):
        for key in self.os_dict_keys:
            os.environ.pop(key)

    def test_execute(self):
        self.command.email_service.send = MagicMock(return_value=True)
        self.assertFalse(self.command.execute())

    def test_failed_execute(self):
        with self.assertRaises(RequestException):
            self.assertFalse(self.command.execute())

    def test_failed_undo(self):
        with self.assertRaises(CommandCantBeUndone):
            self.command.undo()
