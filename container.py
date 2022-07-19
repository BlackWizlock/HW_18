from app.configs.setup_db import db
from app.dao.directorDAO import DirectorDAO
from app.service.director import DirectorService

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
