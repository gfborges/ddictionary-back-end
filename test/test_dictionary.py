from test.assert_utils import assert_dict
from test.pymongomock import PyMongoMock

pets = [
    {
        "title": "cat",
        "group": "feline",
        "domain": "pets",
        "definitions": ["crazy animal", "cute pet"],
        "translations": ["gato", "catze"],
    },
    {
        "title": "cockatoo",
        "group": "bird",
        "domain": "pets",
        "definitions": ["weird pet", "smart animal"],
        "translations": ["cacatua"],
    },
]


def test_health_check(client, mongo):
    res = client.get("/health")
    expected_health = {"api": "ok", "mongo": {"ok": 1.0}}
    assert res.status_code == 200
    assert res.json == expected_health
    assert isinstance(mongo, PyMongoMock)
    assert mongo.is_test()


def test_list_all_entries(client):
    res = client.get("/dictionary/pets/")
    data = res.json
    assert res.status_code == 200
    assert len(data) == 2
    for expected in pets:
        assert expected in data


def test_get_one_entry(client):
    res = client.get("/dictionary/pets/bird/cockatoo")
    data = res.json
    assert res.status_code == 200
    assert data.get("title") == "cockatoo"
    assert data.get("group") == "bird"
    assert data.get("domain") == "pets"
    assert len(data.get("definitions")) == 2
    assert len(data.get("translations")) == 1
