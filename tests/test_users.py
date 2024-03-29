from app.schemas import UserOut
from .database import client, session


def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Hello World!"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "abc@xyz.com", "password": "password123"}
    )
    newUser = UserOut(**res.json())
    assert res.status_code == 201
    assert res.json().get("email") == "abc@xyz.com"


def test_login_user(client):
    res = client.post(
        "/login/", data={"username": "abc@xyz.com", "password": "password123"}
    )
    assert res.status_code == 200
    # assert res.json().get("email") == "abc@xyz.com"
