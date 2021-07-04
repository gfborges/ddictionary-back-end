dog = dict(
    title="The-DOG",
    group="canidae",
    domain="pets",
    definitions=["fun pet", "energetic animal"],
    image="data:image/png;base64,Ab9+/",
)


def test_create_entry(client, bucket):
    created = client.post("/entries", json=dog)
    assert (
        created.status_code == 201
    ), "POST /entries returned wrong status_code"
    _id = created.json.get("id")
    res = client.get("/entries/" + _id)
    assert res.status_code == 200
    data = res.json
    assert data.get("title") == dog["title"]
    assert data.get("group") == dog["group"]
    assert data.get("definitions") == dog["definitions"]
    assert data.get("image") == (
        bucket.url_secure
        + "/ddict/image/upload/v1607/pets/canidae/The-DOG.png"
    )


def test_create_entry_with_translation(client):
    json = dog | {"translations": ["cachorro", "hund"]}
    res = client.post("/entries", json=json)
    assert res.status_code == 201, "POST /entries returned wrong status_code"
    res = client.get("/entries/one", query_string=dog)
    assert res.status_code == 200
    data = res.json
    assert data.get("translations") == json["translations"]


def test_fail_validation_title(client, bad_entry):
    json = dog | bad_entry
    res = client.post("/entries", json=json)
    assert res.status_code == 400
    errors = res.get_json().get("validation_error").get("body_params")
    assert len(errors) == len(bad_entry)
    for error in errors:
        fields = error["loc"]
        assert all(field in bad_entry for field in fields)
