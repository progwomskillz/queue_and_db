import unittest
from unittest.mock import MagicMock

from rabbit_wrapper import RabbitWrapper


class RabbitWrapperTest(unittest.TestCase):
    def setUp(self):
        self.environment_manager = MagicMock()

    def tearDown(self):
        pass

    def test_rabbit_wrapper_init(self):
        RabbitWrapper(self.environment_manager)
        keys = ['RABBIT_HOST', 'RABBIT_QUEUE']
        for key in keys:
            self.environment_manager.get_var_from_env.assert_any_call(key)
