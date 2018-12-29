class DBService:
    def __init__(self, session, user_object):
        self.session = session
        self.user_object = user_object

    def save(self):
        self.session.add(self.user_object)
        self.session.commit()

    def delete(self):
        self.session.delete(self.user_object)
        self.session.commit()
