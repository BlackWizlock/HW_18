from app.configs.setup_db import db
from app.dao.directorDAO import DirectorDAO
from app.dao.genreDAO import GenreDAO
from app.service.director import DirectorService
from app.service.genre import GenreService

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
