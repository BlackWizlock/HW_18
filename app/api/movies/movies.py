import logging

from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from container import movie_service

movies_ns = Namespace('movies', description='Работа с таблицей movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


logger = logging.getLogger("basic")

@movies_ns.route('/')
class MoviesViewByAttr(Resource):
    @movies_ns.param('director_id', 'ID Режиссера для поиска')
    @movies_ns.param('genre_id', 'ID Жанра для поиска')
    @movies_ns.param('year', 'Год для поиска')
    @movies_ns.doc(description='[MOVIE] Работа с базой данный фильмов')
    def get(self):
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)
        year = request.args.get('year', type=int)
        logger.info(f'[GET] Movies Director_id: {director_id} Genre_id:{genre_id} Year: {year}')
        if director_id:
            req = movie_service.get_all_by_director(director_id)
            if not req:
                return f'Not found', 204
            return movies_schema.dump(req), 200
        if genre_id:
            req = movie_service.get_all_by_genre(genre_id)
            if not req:
                return f'Not found', 204
            return movies_schema.dump(req), 200
        if year:
            req = movie_service.get_all_by_year(year)
            if not req:
                return f'Not found', 204
            return movies_schema.dump(req), 200
        return movies_schema.dump(movie_service.get_all()), 200


    def post(self):
        try:
            req_json = request.json
            movie_service.create_movie(req_json)
            return '', 201
        except Exception:
            return '', 404


    def put(self):
        try:
            req_json = request.json
            movie_service.update_movie(req_json)
            return '', 201
        except Exception:
            return '', 404


@movies_ns.route('/<int:movie_id>')
class MovieViewById(Resource):
    @movies_ns.doc(description='[MOVIE] Работа с базой данный фильмов по ID')
    def get(self, movie_id: int):
        logger.info(f'[GET] Movies by id: {movie_id}')
        req = movie_service.get_one(movie_id)
        if req:
            return movie_schema.dump(req), 200
        return f'Not found', 204

    def delete(self, movie_id: int):
        try:
            movie_service.delete_movie(movie_id)
            return f'{movie_id} удалён', 204
        except Exception:
            return '', 404
