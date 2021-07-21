def test_domain_creation(client, mongo):
    created = client.post(
        "/domains",
        json={
            "name": "New Domain",
            "password": "password",
            "slug": "new_domain",
        },
    )
    assert created.status_code == 201
    res = client.get("/domains/new_domain")
    new_domain = res.json
    assert res.status_code == 200
    assert new_domain.get("name") == "New Domain"
    assert new_domain.get("slug") == "new_domain"


def test_domain_creation_password(client, mongo):
    client.post(
        "/domains",
        json={
            "name": "new_domain",
            "password": "password",
            "slug": "new_domain",
        },
    )
    new_domain = mongo.db.domains.find_one({"slug": "new_domain"})
    assert "password" not in new_domain.get("password")
