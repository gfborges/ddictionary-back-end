import os


class MongoConfig:
    HOST = os.getenv("MONGODB_HOST")
    USER = os.getenv("MONGODB_USER")
    PWD = os.getenv("MONGODB_PWD")
    DB = os.getenv("MONGODB_DB")
    PORT = "27017"


class Cloudinary:
    API_KEY = os.getenv("CLOUDINARY_KEY")
    SECRET = os.getenv("CLOUDINARY_SECRET")
    NAME = os.getenv("CLOUDINARY_NAME")


class Auth:
    JWT_SECRET = os.getenv("JWT_SECRET")


class ElasticConfig:
    ES_ACCESS_KEY = os.getenv("ES_ACCESS_KEY")
    ES_SECRET_KEY = os.getenv("ES_SECRET_KEY")
    ES_REGION_NAME = os.getenv("ES_REGION_NAME")
    ES_SERVICE = os.getenv("ES_SERVICE")
    ES_HOST = os.getenv("ES_HOST")
