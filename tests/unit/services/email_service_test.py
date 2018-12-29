import unittest
from unittest.mock import MagicMock
import os

import requests

from services import EmailService


class EmailServiceTest(unittest.TestCase):
    def setUp(self):
        self.EM = MagicMock()
        self.EM.get_var_from_env = MagicMock(return_value='Test')
        self.message = {
            'from': 'Man <man@example.com>',
            'to': 'admin@example.com',
            'subject': 'Success',
            'text': 'Write successfully!'
        }

    def tearDown(self):
        pass

    def test_init(self):
        EmailService(self.EM, self.message)
        keys = ['EMAIL_URL', 'EMAIL_TOKEN']
        for key in keys:
            self.EM.get_var_from_env.assert_any_call(key)

    def test_send(self):
        requests.post = MagicMock(return_value=True)

        email_service = EmailService(self.EM, self.message)
        email_service.send()
        requests.post.assert_called_once()
