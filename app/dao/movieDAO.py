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

    def create_movie(self):
        pass

    def update_movie(self):
        pass

    def delete_movie(self, mid: int):
        self.session.delete(mid)
        self.session.commit()
