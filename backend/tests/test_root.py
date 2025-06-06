from fastapi.testclient import TestClient
import os
import sys
from unittest.mock import Mock

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.app.main import app
import uuid

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Backend FastAPI fonctionne !"


def test_create_user_and_session():
    uname = f"user_{uuid.uuid4().hex[:8]}"
    user_resp = client.post("/users", json={"username": uname})
    assert user_resp.status_code == 200
    user_id = user_resp.json()["user_id"]

    sess_resp = client.post("/sessions", json={"user_id": user_id})
    assert sess_resp.status_code == 200
    assert "session_id" in sess_resp.json()


def test_text_endpoint(monkeypatch):
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.json.return_value = {"response": "ok"}

    def fake_post(url, json):
        assert "generate" in url
        assert json["prompt"] == "hi"
        return mock_resp

    monkeypatch.setattr(
        "backend.app.ollama_client.requests.post",
        fake_post,
    )

    resp = client.post("/txt", json={"prompt": "hi"})

    assert resp.status_code == 200
    assert resp.json()["response"] == "ok"


def test_image_endpoint(monkeypatch):
    def fake_generate(prompt):
        assert prompt == "draw"
        return {"image": "imgdata"}

    monkeypatch.setattr(
        "backend.app.main.stablediffusion_generate_image", fake_generate
    )
    resp = client.post("/img", json={"prompt": "draw"})
    assert resp.status_code == 200
    assert resp.json()["image"] == "imgdata"
