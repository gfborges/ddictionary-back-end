def test_delete_entry(client):
    query = dict(
        domain="pets",
        group="feline",
        title="cat",
    )
    res = client.delete("/entries", query_string=query)
    assert res.status_code == 202
    assert res.json == {}
    res = client.get("/entries/one", query_string=query)
    assert res.status_code == 404
