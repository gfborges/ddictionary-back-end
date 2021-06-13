from flask.app import Flask
from flask.testing import FlaskClient
import pytest
from unittest.mock import patch
from test.pymongomock import PyMongoMock
import app.database.mongo as mongodb
from app import create_app


@pytest.fixture
def mongo():
    with patch.object(mongodb, "mongo", PyMongoMock()):
        yield mongodb.mongo


@pytest.fixture
def app(mongo) -> Flask:
    app = create_app()
    with app.app_context():
        client = mongodb.get_db()
        PyMongoMock.test_data(client)
        yield app


@pytest.fixture
def client(app: FlaskClient):
    yield app.test_client()
