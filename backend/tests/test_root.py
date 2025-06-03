from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.app.backend_server import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Backend FastAPI fonctionne !"


def test_create_user_and_session():
    user_resp = client.post("/users", json={"username": "alice"})
    assert user_resp.status_code == 200
    user_id = user_resp.json()["user_id"]

    sess_resp = client.post("/sessions", json={"user_id": user_id})
    assert sess_resp.status_code == 200
    assert "session_id" in sess_resp.json()
