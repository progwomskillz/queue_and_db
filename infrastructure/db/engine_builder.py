from sqlalchemy import create_engine


class EngineBuilder:
    def __init__(self, environment_manager):
        self.environment_manager = environment_manager

    def build(self):
        db_login = self.environment_manager.get_var_from_env('DB_LOGIN')
        db_password = self.environment_manager.get_var_from_env('DB_PASSWORD')
        db_host = self.environment_manager.get_var_from_env('DB_HOST')
        db_db = self.environment_manager.get_var_from_env('DB_DB')

        engine_string = 'postgresql+psycopg2://' + db_login + ':' \
                        + db_password + '@' + db_host + '/' + db_db
        engine = create_engine(engine_string)

        return engine
