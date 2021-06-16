def test_delete_entry(client):
    cat_id = "60c809cbec2fc163dbda3666"
    res = client.delete("/entries/" + cat_id)
    assert res.status_code == 202
    assert res.json == {}
    res = client.get("/entries/" + cat_id)
    assert res.status_code == 404
