def test_health_check(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json == {
        "api": "ok",
        "mongo": {"ok": 1.0},
        "cloudinary": "ok",
    }
