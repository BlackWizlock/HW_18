from app.dao.model.director import Director


# CRUD
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did: int):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()
