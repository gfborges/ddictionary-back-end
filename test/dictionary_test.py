from unittest.mock import patch

from test.pymongomock import PyMongoMock
from unittest import TestCase
import app.database.mongo
from app import create_app


@patch.object(app.database.mongo, "mongo", PyMongoMock())
class TestDictionary(TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_health_check(self):
        res = self.client.get("/dictionary/")
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(res.json, {"mongo": {"ok": 1.0}})
        self.assertIsInstance(app.database.mongo.get_db(), PyMongoMock)
