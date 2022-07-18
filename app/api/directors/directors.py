from flask_restx import Resource, Namespace

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):

    # CRUD
    def create(self):
        return "", 200

    def read(self):
        return "", 200

    def read_id(self, uid):
        return "", 200

    def update(self):
        return "", 200

    def delete(self):
        return "", 200
