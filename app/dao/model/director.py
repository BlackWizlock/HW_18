from marshmallow import Schema, fields

from app.configs.setup_db import db


class Director(db.Model):
    __tablename__ = "director"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
