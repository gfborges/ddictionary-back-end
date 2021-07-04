def test_domain_creation(client):
    created = client.post(
        "/domains",
        json={
            "name": "new_domain",
            "password": "password",
        },
    )
    assert created.status_code == 200
    res = client.get("/domains/new_domain")
    new_domain = res.json
    assert res.status_code == 200
    assert new_domain.get("name") == "new_domain"


def test_domain_creation(client, mongo):
    client.post(
        "/domains",
        json={
            "name": "new_domain",
            "password": "password",
        },
    )
    new_domain = mongo.db.domains.find_one({"name": "new_domain"})
    assert "password" not in new_domain.get("password").decode()
