import collections
from app.database.mongo import get_mongo_uri
import subprocess

from flask_pymongo import PyMongo


class DataLoader:
    collections = ["entries", "domains"]

    @classmethod
    def load(cls):
        uri = get_mongo_uri()
        for collection in cls.collections:
            subprocess.run(
                [
                    "docker",
                    "exec",
                    "test-mongodb",
                    "mongoimport",
                    f"--uri={uri}",
                    "--file",
                    f"/test/data/{collection}.json",
                    "--jsonArray",
                ]
            )

    @classmethod
    def destroy(cls, mongo):
        for collection in cls.collections:
            mongo.db[collection].delete_many({})
