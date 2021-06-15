from mongomock import MongoClient
from test.data import DataLoader
import mongomock


class PyMongoMock(MongoClient):
    def init_app(self, _):
        client = super().__init__()
        return client

    def is_test(self) -> bool:
        return True

    @staticmethod
    def test_data(client: mongomock.MongoClient):
        DataLoader.load(client)
