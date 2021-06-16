def test_update_entry(client):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(title="kitty")
    updated = client.put("/entries/" + cat_id, json=update_data)
    assert updated.status_code == 204
    res = client.get("/entries/" + cat_id)
    kitty = res.json
    assert kitty.get("id") == cat_id
    assert kitty.get("title") == update_data["title"]
