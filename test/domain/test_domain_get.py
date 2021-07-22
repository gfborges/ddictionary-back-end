def test_get_domain(client):
    res = client.get("/domains/pets")
    data = res.json
    assert res.status_code == 200
    assert data.get("name") == "Pets"
    assert data.get("slug") == "pets"
    assert data.get("groups") == ["feline", "bird"]
    assert data.get("password") is None


def test_get_inexistant_domain(client):
    res = client.get("/domains/neverland")
    data = res.json
    assert res.status_code == 404
    assert data.get("message") == "404 Not Found: Domain not found"
