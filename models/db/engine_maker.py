from sqlalchemy import create_engine

from models.environment_settings import EnvironmentSettings


class EngineMaker:
    @staticmethod
    def make_engine():
        db_login = EnvironmentSettings._get_var_from_env('DB_LOGIN')
        db_password = EnvironmentSettings._get_var_from_env('DB_PASSWORD')
        db_host = EnvironmentSettings._get_var_from_env('DB_HOST')
        db_db = EnvironmentSettings._get_var_from_env('DB_DB')

        engine_string = 'postgresql+psycopg2://' + db_login + ':'
        engine_string += db_password + '@' + db_host + '/' + db_db
        engine = create_engine(engine_string)

        return engine
