import unittest
import os

from models.rabbit_wrapper import RabbitWrapper
from exceptions.environment.variable_cant_be_import import VariableCantBeImport


class RabbitWrapperTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rabbit_wrapper_init(self):
        os_dict_keys = ['RABBIT_HOST', 'RABBIT_QUEUE']
        for key in os_dict_keys:
            os.environ[key] = 'test_var'

        rabbit_wrapper = RabbitWrapper()

        for key in os_dict_keys:
            os.environ.pop(key)

    def test_failed_rabbit_wrapper_init(self):
        with self.assertRaises(VariableCantBeImport):
            rabbit_wrapper = RabbitWrapper()
