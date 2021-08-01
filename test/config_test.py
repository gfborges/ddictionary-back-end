from _pytest import config


from app.config import MongoConfig


class TestMongoConfig(MongoConfig):
    HOST = "localhost"
