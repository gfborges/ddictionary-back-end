from flask_jwt_extended.utils import decode_token
from test.auth.utils import get_headers


def test_username_required(client):
    no_username = {"password": "password"}
    empty_username = no_username | {"username": ""}
    empty_password_res = client.post("/auth", json=empty_username)
    no_password_res = client.post("/auth", json=no_username)
    assert empty_password_res.status_code == 400
    assert no_password_res.status_code == 400


def test_password_required(client):
    no_password = {"username": "pets"}
    empty_password = no_password | {"password": ""}
    empty_password_res = client.post("/auth", json=empty_password)
    no_password_res = client.post("/auth", json=no_password)
    assert empty_password_res.status_code == 400
    assert no_password_res.status_code == 400


def test_login_success_with_correct_password_and_username(client):
    no_password = {
        "username": "pets",
        "password": "secret_password",
    }
    res = client.post("/auth", json=no_password)
    assert res.status_code == 200
    access_token = res.json.get("access_token")
    recieved = decode_token(access_token, allow_expired=True)
    assert recieved.get("sub") == "pets"
    assert recieved.get("_id") == "c23f57d571bc787f7a7a87a0"


def test_login_fails_with_incorrect_password_and_username(client):
    no_password = {
        "username": "pets",
        "password": "unsafe_password",
    }
    res = client.post("/auth", json=no_password)
    assert res.status_code == 403
    assert (
        res.json.get("message") == "403 Forbidden: Wrong username or password"
    )


def test_returns_user(client, jwt):
    res = client.get("/auth/me", headers=get_headers(jwt))
    assert res.status_code == 200
    assert res.json.get("slug") == "pets"
