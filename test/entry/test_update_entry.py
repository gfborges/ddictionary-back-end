from test.auth.utils import get_headers


def test_update_entry(client, jwt):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(title="kitty")
    updated = client.put(
        "/entries/" + cat_id,
        json=update_data,
        headers=get_headers(jwt),
    )
    assert updated.status_code == 201
    res = client.get("/entries/" + cat_id)
    kitty = res.json
    assert res.status_code == 200
    assert kitty.get("_id") == cat_id
    assert kitty.get("title") == update_data["title"]


def test_dont_update_domain(client, jwt):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(domain="domestic-animals")
    updated = client.put(
        "/entries/" + cat_id,
        json=update_data,
        headers=get_headers(jwt),
    )
    assert updated.status_code == 404
    res = client.get("/entries/" + cat_id)
    kitty = res.json
    assert res.status_code == 200
    assert kitty.get("_id") == cat_id
    assert kitty.get("domain") == "pets"


def test_dont_update_id(client, jwt):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(_id="666666cbec2fc163dbda3666")
    updated = client.put(
        "/entries/" + cat_id,
        json=update_data,
        headers=get_headers(jwt),
    )
    assert updated.status_code == 404
    res = client.get("/entries/" + update_data["_id"])
    assert res.status_code == 404


def test_dont_update_entry_without_auth(client):
    cat_id = "60c809cbec2fc163dbda3666"
    update_data = dict(_id="666666cbec2fc163dbda3666")
    updated = client.put(
        "/entries/" + cat_id,
        json=update_data,
    )
    assert updated.status_code == 401


def test_dont_update_entry_of_other_domain(client, jwt):
    experience_id = "80a16c08752a59e40696660c"
    res = client.put(
        "/entries/" + experience_id,
        headers=get_headers(jwt),
        json={"title": "pimba"},
    )
    assert res.status_code == 405
    res = client.get("/entries/" + experience_id)
    assert res.status_code == 200
    assert res.json.get("title") == "experience"
