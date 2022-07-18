from flask_restx import Resource, Namespace

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "", 200

    def get_id(self, uid):
        return "", 200
