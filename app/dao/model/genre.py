from marshmallow import Schema, fields

from app.configs.setup_db import db


class Genre(db.Model):
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
