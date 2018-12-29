import os

from infrastructure.exceptions import VariableCantBeImport


class EnvironmentManager:
    def __init__(self):
        pass

    def get_var_from_env(self, key):
        try:
            return os.environ[key]
        except KeyError:
            raise VariableCantBeImport('Set ' + key + ' environment variable')
