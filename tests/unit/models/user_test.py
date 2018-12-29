import unittest

from models.db import User, DBTableBase


class UserTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_relationship(self):
        user = User()
        self.assertIsInstance(user, DBTableBase)
