import unittest

from sqlalchemy.orm.session import Session

from models.db.session_maker import SessionMaker


class SessionMakerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_session_init(self):
        session = SessionMaker.make_session(True)
        self.assertIsInstance(session, Session)
