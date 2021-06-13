import os


class Mongo:
    HOST = os.getenv("MONGODB_HOST")
    USER = os.getenv("MONGODB_USER")
    PWD = os.getenv("MONGODB_PWD")
    DB = os.getenv("MONGODB_DB")
