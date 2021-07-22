from test.auth.utils import get_headers

cat_id = "60c809cbec2fc163dbda3666"


def test_delete_entry(client, jwt):
    res = client.delete(
        "/entries/" + cat_id,
        headers=get_headers(jwt),
    )
    assert res.status_code == 202
    assert res.json == {}
    res = client.get("/entries/" + cat_id)
    assert res.status_code == 404


def test_dont_delete_entry_of_other_domain(client, jwt):
    experience_id = "80a16c08752a59e40696660c"
    res = client.delete(
        "/entries/" + experience_id,
        headers=get_headers(jwt),
    )
    assert res.status_code == 404
    res = client.get("/entries/" + experience_id)
    assert res.status_code == 200


def test_dont_delete_entry_without_auth(client):
    res = client.delete("/entries/" + cat_id)
    assert res.status_code == 401
