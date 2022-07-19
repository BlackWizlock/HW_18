from app.dao.directorDAO import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did: int):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()
