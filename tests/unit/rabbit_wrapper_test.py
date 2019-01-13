import unittest
from unittest.mock import MagicMock

from rabbit_wrapper import RabbitWrapper


class RabbitWrapperTest(unittest.TestCase):
    def setUp(self):
        self.EM = MagicMock()

    def tearDown(self):
        pass

    def test_rabbit_wrapper_init(self):
        RabbitWrapper(self.EM)
        keys = ['RABBIT_HOST', 'RABBIT_QUEUE']
        for key in keys:
            self.EM.get_var_from_env.assert_any_call(key)
