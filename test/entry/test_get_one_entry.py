def test_get_one_entry(client):
    res = client.get("/entries/pets/bird/cockatoo")
    data = res.json
    assert res.status_code == 200
    assert data.get("title") == "cockatoo"
    assert data.get("group") == "bird"
    assert data.get("domain") == "pets"
    assert len(data.get("definitions")) == 2
    assert len(data.get("translations")) == 1
