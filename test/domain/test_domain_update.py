from test.auth.utils import get_headers


def test_update_domain_group(client, jwt):
    updated = client.put(
        "/domains", json={"group": "dog"}, headers=get_headers(jwt)
    )
    res = client.get("/domains/pets")
    pets = res.json
    assert updated.status_code == 201
    assert pets.get("groups") == ["feline", "bird", "dog"]


def test_fail_update(client):
    updated = client.put("/domains", json={"group": "ape"})
    assert updated.status_code == 401
    res = client.get("/domains/pets")
    pets = res.json
    assert pets.get("groups") == ["feline", "bird"]
