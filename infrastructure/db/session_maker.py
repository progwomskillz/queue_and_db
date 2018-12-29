from sqlalchemy.orm import sessionmaker


class SessionMaker:
    @staticmethod
    def make_session(engine):
        session = sessionmaker(bind=engine)
        return session()
