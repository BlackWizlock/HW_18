from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from container import director_service

directors_ns = Namespace('directors', description='Работа с таблицей directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):

    # CRUD
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):

    # CRUD
    def get(self, did: int):
        if not isinstance(did, int):
            return 'Invalid type of instance', 404
        director = director_service.get_one(did)
        if not director:
            return f'Not found', 204
        return director_schema.dump(director), 200
