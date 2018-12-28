import unittest
from unittest.mock import MagicMock

from models.services.db_service import DBService
from models.db.session_maker import SessionMaker
from models.db.user import User


class DBServiceTest(unittest.TestCase):
    def setUp(self):
        session = SessionMaker.make_session(True)
        session.commit = MagicMock(return_value=True)
        user = User()
        self.db = DBService(session, user)

    def tearDown(self):
        pass

    def test_save(self):
        self.db.save()

    def test_delete(self):
        self.db.delete()
