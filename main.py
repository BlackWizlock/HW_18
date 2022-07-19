# Flask and Flask-restx importing
from flask import Flask
from flask_restx import Api

# API views importing
from app.api.directors.directors import directors_ns
from app.api.genres.genres import genres_ns
from app.api.movies.movies import movies_ns

# Config for flask factory
from app.configs.config import Config

# DB importing
from app.configs.setup_db import db


# Application creating and pushing config as a context -> return flask instance
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


# Application configuration, db init, restx init, namespace assignment
def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)


if __name__ == '__main__':
    # Config instance creating
    app_config = Config()
    # app instance creating and config instance pushing into it
    app = create_app(app_config)
    # init db, restx according to app instance which was created before
    configure_app(app)
    # simple application running
    app.run()
