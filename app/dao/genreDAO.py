from app.dao.model.genre import Genre


# сRud - only read was used
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid: int):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()
