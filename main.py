from flask_restx import Api

from flask import Flask

from app.api.directors.directors import directors_ns
from app.api.genres.genres import genres_ns
from app.api.movies.movies import movies_ns
from app.configs.config import Config
from app.configs.setup_db import db


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()
