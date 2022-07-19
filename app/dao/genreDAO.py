from app.dao.model.genre import Genre


# CRUD
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid: int):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, data):
        did = data.get('id')
        genre = self.get_one(did)
        genre.name = data.get('name')
        self.session.add(genre)
        self.session.commit()
        return genre

    def update_partial(self, data):
        gid = data.get('id')
        genre = self.get_one(gid)
        if data.get('name') in data:
            genre.name = data.get('name')
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, gid: int):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()
