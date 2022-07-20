from app.dao.movieDAO import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid: int):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_all_by_director(self, director: int):
        return self.dao.get_all_by_director(director)

    def get_all_by_genre(self, genre: int):
        return self.dao.get_all_by_genre(genre)

    def get_all_by_year(self, year: int):
        return self.dao.get_all_by_year(year)

    def create_movie(self, data):
        return self.dao.create_movie(data)

    def update_movie(self, data):
        return self.dao.update_movie(data)

    def delete_movie(self, mid: int):
        self.dao.delete_movie(self.dao.get_one(mid))
