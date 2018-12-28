import unittest
from unittest.mock import MagicMock
import os

import requests

from models.services.email_service import EmailService
from exceptions.environment.variable_cant_be_import import VariableCantBeImport


class EmailServiceTest(unittest.TestCase):
    def setUp(self):
        message = {
            'from': 'Man <man@example.com>',
            'to': 'admin@example.com',
            'subject': 'Success',
            'text': 'Write successfully!'
        }
        self.email_service = EmailService(message)
        requests.post = MagicMock(return_value=True)

    def tearDown(self):
        pass

    def test_send(self):
        os_dict_keys = ['EMAIL_URL', 'EMAIL_TOKEN']
        for key in os_dict_keys:
            os.environ[key] = 'test_var'

        self.email_service.send()

        for key in os_dict_keys:
            os.environ.pop(key)

    def test_failed_send(self):
        with self.assertRaises(VariableCantBeImport):
            self.email_service.send()
