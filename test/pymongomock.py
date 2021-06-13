from mongomock import MongoClient


class PyMongoMock(MongoClient):
    def init_app(self, _):
        return super().__init__()

    def is_test(self) -> bool:
        return True
