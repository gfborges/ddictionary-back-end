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


def test_list_all_entries(client):
    res = client.get("/entries/pets")
    data = res.json
    assert res.status_code == 200
    assert len(data) == 2
    for expected in pets:
        assert expected in data
