import unittest
from unittest.mock import MagicMock
import os

from models import Invoker
from models.db import EngineMaker, SessionMaker, User
from models.services import DBService, EmailService
from commands import WriteToDbCommand, SendEmailCommand
from exceptions.commands import CommandRuntimeError


class InvokerTest(unittest.TestCase):
    def setUp(self):
        commands = []

        self.os_dict_keys = ['DB_LOGIN', 'DB_PASSWORD', 'DB_HOST', 'DB_DB',
                             'EMAIL_URL', 'EMAIL_TOKEN']
        for key in self.os_dict_keys:
            os.environ[key] = 'test_var'

        engine = EngineMaker.make_engine()
        session = SessionMaker.make_session(engine)
        user_object = User(id=1, first_name='Nik', last_name='S.')
        db_service = DBService(session, user_object)
        write_to_db_command = WriteToDbCommand(db_service)
        commands.append(write_to_db_command)

        message = {
            'from': 'Man <man@example.com>',
            'to': 'admin@example.com',
            'subject': 'Success',
            'text': 'Write successfully!'
        }
        email_service = EmailService(message)
        send_email_command = SendEmailCommand(email_service)
        commands.append(send_email_command)

        self.invoker = Invoker(commands)

    def tearDown(self):
        for key in self.os_dict_keys:
            os.environ.pop(key)

    def test_execute_commands(self):
        self.invoker.commands[0].db_service.save = MagicMock(return_value=True)
        self.invoker.commands[1].email_service.send = MagicMock(
            return_value=True)
        self.invoker.execute_commands()

    def test_failed_execute_commands(self):
        with self.assertRaises(CommandRuntimeError):
            self.invoker.execute_commands()
