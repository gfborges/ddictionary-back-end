from mongomock import MongoClient
import mongomock
import os
import json
import test


class PyMongoMock(MongoClient):
    def init_app(self, _):
        client = super().__init__()
        return client

    def is_test(self) -> bool:
        return True

    @staticmethod
    def test_data(client: mongomock.MongoClient):
        loader = DataLoader(client)
        loader.load()


class DataLoader:
    data_folder = os.path.join(os.path.dirname(test.__file__), "data")

    def __init__(self, client):
        self.client = client

    def load(self):
        for collection_filename in os.listdir(self.data_folder):
            collection_file = os.path.join(
                self.data_folder, collection_filename
            )
            with open(collection_file, "r") as collection:
                collection_name = collection_filename[:-5]
                collection_data = json.load(collection)
                self.client.db[collection_name].insert_many(collection_data)
