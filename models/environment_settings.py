import os

from exceptions.environment.variable_cant_be_import import VariableCantBeImport


class EnvironmentSettings:
    @staticmethod
    def get_var_from_env(key):
        try:
            return os.environ[key]
        except KeyError:
            raise VariableCantBeImport('Set ' + key + ' environment variable')
