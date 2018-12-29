import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm.session import Session

from infrastructure.db import SessionBuilder


class SessionBuilderTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_build(self):
        engine = MagicMock()
        session_builder = SessionBuilder(engine)
        session = session_builder.build()
        self.assertIsInstance(session, Session)
