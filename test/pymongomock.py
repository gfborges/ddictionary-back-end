from test.data import DataLoader


class PyMongoMock:
    @staticmethod
    def load_test_data(client):
        DataLoader.load(client)
