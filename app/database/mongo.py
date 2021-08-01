from flask_pymongo import PyMongo
from app.config import MongoConfig
from flask import Flask

mongo = PyMongo()


def get_db():
    return mongo


def mongo_health():
    return get_db().db.command("ping")


def get_mongo_uri():
    return f"mongodb://{MongoConfig.USER}:{MongoConfig.PWD}@{MongoConfig.HOST}:27017/{MongoConfig.DB}?authSource=admin"


def config_mongo(app: Flask):
    app.config["MONGO_URI"] = get_mongo_uri()
    mongo.init_app(app)
