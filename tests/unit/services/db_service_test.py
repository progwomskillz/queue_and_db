import unittest
from unittest.mock import MagicMock

from services import DBService


class DBServiceTest(unittest.TestCase):
    def setUp(self):
        self.session = MagicMock()
        self.user_object = MagicMock()
        self.db_service = DBService(self.session, self.user_object)

    def tearDown(self):
        pass

    def test_save(self):
        self.db_service.save()
        self.session.add.assert_called_once_with(self.user_object)
        self.session.commit.assert_called_once()

    def test_delete(self):
        self.db_service.delete()
        self.session.delete.assert_called_once_with(self.user_object)
        self.session.commit.assert_called_once()
