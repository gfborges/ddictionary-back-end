from flask_pymongo import PyMongo
from app.config import Mongo
from flask import Flask

mongo = PyMongo()


def get_db():
    return mongo


def get_mongo_uri():
    return f"mongodb://{Mongo.USER}:{Mongo.PWD}@{Mongo.HOST}:27017/{Mongo.DB}?authSource=admin"


def config_mongo(app: Flask):
    app.config["MONGO_URI"] = get_mongo_uri()
    mongo.init_app(app)
