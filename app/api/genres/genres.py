from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):

    # CRUD
    def get(self):
        all_genres = genre_dao.get_all()
        return genre_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        genres_dao.create(req_json)
        return "", 201


@genres_ns.route('/<int:gid>')
class GenreView(Resource):

    # CRUD
    def get(self, gid: int):
        director = genre_dao.get_one(gid)
        return genre_schema.dump(director), 200

    def put(self, gid: int):
        req_json = request.json
        req_json['id'] = gid
        genre_dao.update(req_json)
        return "", 204

    def patch(self, gid: int):
        req_json = request.json
        req_json['id'] = gid
        genre_dao.update_partial(req_json)
        return "", 200

    def delete(self, did: int):
        # director =
        return "", 200
