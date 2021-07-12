def test_get_one_entry(client):
    query = dict(
        domain="pets",
        group="bird",
        title="cockatoo",
    )
    res = client.get("/entries/one", query_string=query)
    data = res.json
    assert res.status_code == 200
    assert data.get("title") == "cockatoo"
    assert data.get("group") == "bird"
    assert data.get("domain") == "pets"
    assert len(data.get("definitions")) == 2
    assert len(data.get("translations")) == 1
    assert data.get("created_at") == "1970-01-01T12:30:59"


def test_get_non_existant_entry(client):
    query = dict(
        domain="pets",
        group="myth",
        title="yeti",
    )
    res = client.get("/entries/one", query_string=query)
    data = res.json
    assert res.status_code == 404
    assert "Entry Not Found" in data.get("message")


def test_get_by_id(client, mongo):
    _id = "80a16c08752a59e40696660c"
    res = client.get("/entries/" + _id)
    data = res.json
    assert res.status_code == 200
    assert data.get("_id") == _id
