def test_update_entry(client):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(title="kitty")
    updated = client.put("/entries/" + cat_id, json=update_data)
    assert updated.status_code == 204
    res = client.get("/entries/" + cat_id)
    kitty = res.json
    assert res.status_code == 200
    assert kitty.get("id") == cat_id
    assert kitty.get("title") == update_data["title"]


def test_dont_update_domain(client):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(domain="domestic-animals")
    updated = client.put("/entries/" + cat_id, json=update_data)
    assert updated.status_code == 204
    res = client.get("/entries/" + cat_id)
    kitty = res.json
    assert res.status_code == 200
    assert kitty.get("id") == cat_id
    assert kitty.get("domain") == "pets"


def test_dont_update_id(client):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(_id="666666cbec2fc163dbda3666")
    updated = client.put("/entries/" + cat_id, json=update_data)
    assert updated.status_code == 204
    res = client.get("/entries/" + update_data["_id"])
    assert res.status_code == 404
