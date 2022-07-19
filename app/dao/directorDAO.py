from app.dao.model.director import Director


# CRUD
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did: int):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, data):
        did = data.get('id')
        director = self.get_one(did)
        director.name = data.get('name')
        self.session.add(director)
        self.session.commit()
        return director

    def update_partial(self, data):
        did = data.get('id')
        director = self.get_one(did)
        if data.get('name') in data:
            director.name = data.get('name')
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did: int):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

