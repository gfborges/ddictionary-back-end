dog = dict(title="The-DOG", group="canidae")


def test_create_entry(client):
    res = client.post("/entries/pets", json=dog)
    assert (
        res.status_code == 201
    ), "POST /entries/<domain> returned wrong status_code"
    res = client.get("/entries/pets/canidae/The-DOG")
    assert res.status_code == 200
    data = res.json
    assert data.get("title") == dog["title"]
    assert data.get("group") == dog["group"]


def test_fail_validation_title(client, bad_entry):
    json = dog | bad_entry
    res = client.post("/entries/pets", json=json)
    assert res.status_code == 400
    errors = res.get_json().get("validation_error").get("body_params")
    assert len(errors) == len(bad_entry)
    for error in errors:
        fields = error["loc"]
        assert all(field in bad_entry for field in fields)
