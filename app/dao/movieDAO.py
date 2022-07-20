from app.dao.model.movie import Movie


# CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid: int):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_by_director(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_all_by_genre(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_all_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create_movie(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update_movie(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete_movie(self, mid: int):
        self.session.delete(mid)
        self.session.commit()
