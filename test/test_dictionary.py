from test.pymongomock import PyMongoMock
from flask_pymongo import PyMongo


def test_health_check(client, mongo):
    res = client.get("/health")
    expected_health = {"api": "ok", "mongo": {"ok": 1.0}}
    assert res.status_code == 200
    assert res.json == expected_health
    assert isinstance(mongo, PyMongoMock)
    assert mongo.is_test()
