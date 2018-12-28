import unittest

from sqlalchemy.ext.declarative import declarative_base

from models.db.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_relationship(self):
        user = User()
        db_table_base = declarative_base()
        self.assertIsInstance(user, db_table_base)
