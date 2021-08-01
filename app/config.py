import os


class MongoConfig:
    HOST = os.getenv("MONGODB_HOST")
    USER = os.getenv("MONGODB_USER")
    PWD = os.getenv("MONGODB_PWD")
    DB = os.getenv("MONGODB_DB")


class Cloudinary:
    API_KEY = os.getenv("CLOUDINARY_KEY")
    SECRET = os.getenv("CLOUDINARY_SECRET")
    NAME = os.getenv("CLOUDINARY_NAME")


class Auth:
    JWT_SECRET = os.getenv("JWT_SECRET")
