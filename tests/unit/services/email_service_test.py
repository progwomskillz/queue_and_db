import unittest
from unittest.mock import MagicMock
import os

import requests

from models.services import EmailService
from exceptions.environment import VariableCantBeImport


class EmailServiceTest(unittest.TestCase):
    def setUp(self):
        self.message = {
            'from': 'Man <man@example.com>',
            'to': 'admin@example.com',
            'subject': 'Success',
            'text': 'Write successfully!'
        }
        requests.post = MagicMock(return_value=True)

    def tearDown(self):
        pass

    def test_send(self):
        os_dict_keys = ['EMAIL_URL', 'EMAIL_TOKEN']
        for key in os_dict_keys:
            os.environ[key] = 'test_var'

        email_service = EmailService(self.message)
        email_service.send()

        for key in os_dict_keys:
            os.environ.pop(key)

    def test_failed_send(self):
        with self.assertRaises(VariableCantBeImport):
            email_service = EmailService(self.message)
            email_service.send()
