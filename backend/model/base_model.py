from peewee import Model

from backend.config import db


class BaseModel(Model):
    class Meta:
        database = db
