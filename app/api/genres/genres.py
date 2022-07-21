from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from container import genre_service

genres_ns = Namespace('genres', description='Работа с таблицей genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):

    # CRUD
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):

    # CRUD
    def get(self, gid: int):
        if not isinstance(gid, int):
            return 'Invalid type of instance', 404
        genre = genre_service.get_one(gid)
        if genre:
            return genre_schema.dump(genre), 200
        return f'Not found', 204
