from app.dao.genreDAO import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid: int):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()
