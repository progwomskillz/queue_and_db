import os

from infrastructure.exceptions import VariableCantBeFound


class EnvironmentManager:
    def __init__(self):
        pass

    def get_var_from_env(self, key):
        try:
            return os.environ[key]
        except KeyError:
            raise VariableCantBeFound('Set ' + key + ' environment variable')
