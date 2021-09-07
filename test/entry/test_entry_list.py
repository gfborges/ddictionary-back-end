pets = [
    {
        "_id": "60c809cbec2fc163dbda3666",
        "title": "cat",
        "group": "feline",
        "domain": "pets",
        "definitions": "crazy animal",
        "created_at": "1970-01-01T00:00:00",
    },
    {
        "_id": "af24d828d3622d8660c80a01",
        "title": "cockatoo",
        "group": "bird",
        "domain": "pets",
        "definitions": "weird pet",
        "created_at": "1970-01-01T12:30:59",
    },
]


def test_list_all_entries(client):
    query = dict(domain="pets")
    res = client.get("/entries/all", query_string=query)
    data = res.json
    assert res.status_code == 200
    assert len(data) == 2
    for expected in pets:
        assert expected in data
