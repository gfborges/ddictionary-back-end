dog = dict(
    title="The-DOG",
    group="canidae",
    domain="pets",
)


def test_create_entry(client):
    res = client.post("/entries", json=dog)
    assert res.status_code == 201, "POST /entriesreturned wrong status_code"
    res = client.get("/entries", query_string=dog)
    assert res.status_code == 200
    data = res.json
    assert data.get("title") == dog["title"]
    assert data.get("group") == dog["group"]


def test_fail_validation_title(client, bad_entry):
    json = dog | bad_entry
    res = client.post("/entries", json=json)
    assert res.status_code == 400
    errors = res.get_json().get("validation_error").get("body_params")
    assert len(errors) == len(bad_entry)
    for error in errors:
        fields = error["loc"]
        assert all(field in bad_entry for field in fields)
