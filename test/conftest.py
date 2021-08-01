import json

from flask_pymongo import PyMongo
from test.data import DataLoader
from test.cloudinary_mock import CloudinaryMock
from flask.app import Flask
from flask.testing import FlaskClient
from flask_jwt_extended import create_access_token
import pytest
from unittest.mock import patch
import app.database.mongo as mongodb
import app.database.cloudinarycfg as cloudinarycfg
from app import create_app
from test.config_test import TestMongoConfig

setup = 0
teardown = 0

bucket_mock = CloudinaryMock()


@pytest.fixture(scope="session")
def config():
    with patch("app.config.MongoConfig", TestMongoConfig):
        yield TestMongoConfig


@pytest.fixture(scope="function")
def mongo():
    DataLoader.load()
    yield mongodb.mongo
    DataLoader.destroy(mongodb.mongo)


@pytest.fixture
def bucket():
    with patch.object(cloudinarycfg, "cloudinary_uploader", bucket_mock):
        yield bucket_mock


@pytest.fixture(scope="function")
def app(bucket) -> Flask:
    with patch("app.database.mongo.MongoConfig", TestMongoConfig):
        app = create_app()
        with app.app_context():
            yield app


@pytest.fixture()
def jwt(app):
    yield create_access_token(identity="pets")


@pytest.fixture()
def client(app: FlaskClient, mongo: PyMongo):
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
