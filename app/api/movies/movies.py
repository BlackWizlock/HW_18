from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from container import movie_service

movies_ns = Namespace('movies', description='Работа с таблицей movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('')
class MoviesViewByAttr(Resource):
    @movies_ns.param('director_id', 'ID Режиссера для поиска')
    @movies_ns.param('genre_id', 'ID Жанра для поиска')
    @movies_ns.param('year', 'Год для поиска')
    @movies_ns.doc(description='[MOVIE] Работа с базой данный фильмов')
    def get(self):
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)
        year = request.args.get('year', type=int)
        if director_id:
            return movies_schema.dump(movie_service.get_all_by_director(director_id)), 200
        if genre_id:
            return movies_schema.dump(movie_service.get_all_by_genre(genre_id)), 200
        if year:
            return movies_schema.dump(movie_service.get_all_by_year(year)), 200
        return movies_schema.dump(movie_service.get_all()), 200


@movies_ns.route('/<int:movie_id>')
class MovieViewById(Resource):
    @movies_ns.doc(description='[MOVIE] Работа с базой данный фильмов по ID')
    def get(self, movie_id: int):
        return movie_schema.dump(movie_service.get_one(movie_id)), 200

    def delete(self, movie_id: int):
        movie_service.delete_movie(movie_id)
        return f'{movie_id} удалён', 204

    # TODO: add PUT method, POST method for movies
