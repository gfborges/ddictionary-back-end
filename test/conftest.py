import pytest
from pytest_elasticsearch import factories
from flask_pymongo import PyMongo
from flask.app import Flask
from flask.testing import FlaskClient
from flask_jwt_extended import create_access_token
from unittest.mock import patch

import app.database.escfg as escfg
import app.database.mongo as mongodb
import app.database.cloudinarycfg as cloudinarycfg
from test.escfg_test import config_es_test
from test.config_test import TestMongoConfig
from test.cloudinary_mock import CloudinaryMock
from test.data import DataLoader

setup = 0
teardown = 0

bucket_mock = CloudinaryMock()
es_proc = factories.elasticsearch_proc(
    port=None, logs_prefix="/tmp", index_store_type="fs"
)
es = factories.elasticsearch("es_proc")


@pytest.fixture()
def config_es():
    with patch("app.config_es") as config_es:
        config_es.return_value = config_es_test()
        yield config_es


@pytest.fixture()
def es():
    with patch.object(escfg, "es", es):
        yield es


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
def app(bucket, es, config_es) -> Flask:
    from app import create_app

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
