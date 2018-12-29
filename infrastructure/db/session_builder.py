from sqlalchemy.orm import sessionmaker


class SessionBuilder:
    def __init__(self, engine):
        self.engine = engine

    def build(self):
        session = sessionmaker(bind=self.engine)
        return session()
