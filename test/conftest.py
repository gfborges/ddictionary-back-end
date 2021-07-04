from test.cloudinary_mock import CloudinaryMock
from flask.app import Flask
from flask.testing import FlaskClient
import pytest
from unittest.mock import patch
from test.pymongomock import PyMongoMock
import app.database.mongo as mongodb
import app.database.cloudinarycfg as cloudinarycfg
from app import create_app

setup = 0
teardown = 0

mongodb_mock = PyMongoMock()
bucket_mock = CloudinaryMock()


@pytest.fixture
def mongo():
    with patch.object(mongodb, "mongo", mongodb_mock):
        yield mongodb.mongo


@pytest.fixture
def bucket():
    with patch.object(cloudinarycfg, "cloudinary_uploader", bucket_mock):
        yield bucket_mock


@pytest.fixture(scope="function")
def app(mongo, bucket) -> Flask:
    app = create_app()
    with app.app_context():
        PyMongoMock.test_data(mongo)
        yield app


@pytest.fixture()
def client(app: FlaskClient):
    yield app.test_client()


def pytest_generate_tests(metafunc):
    if "bad_entry" in metafunc.fixturenames:
        metafunc.parametrize(
            "bad_entry",
            [
                {"title": ""},
                {"group": ""},
                {"title": "@ entry"},
                {"title": "a &ntry"},
                {"group": "@ group"},
                {"group": "a gr*up"},
            ],
        )
