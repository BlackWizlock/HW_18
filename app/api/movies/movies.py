from flask_restx import Resource, Namespace

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "", 200

    def get_id(self, uid):
        return "", 200
