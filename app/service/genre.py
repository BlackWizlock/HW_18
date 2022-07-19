from app.dao.genreDAO import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, did: int):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data.get('id')
        genre = self.get_one(did)
        genre.name = data.get('name')
        self.dao.update(genre)

    def update_partial(self, data):
        did = data.get('id')
        genre = self.get_one(did)
        if 'name' in data:
            genre.name = data.get('name')
        self.dao.update(genre)
