from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "", 200

    def put(self):
        return "", 200


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        return f"{uid}", 200
