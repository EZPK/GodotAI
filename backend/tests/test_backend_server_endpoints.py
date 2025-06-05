from fastapi.testclient import TestClient
import os
import sys
from unittest.mock import Mock

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.app.main import app

client = TestClient(app)


def test_gen_text(monkeypatch):
    def fake_post(url, json):
        assert "generate" in url
        assert json["model"]
        assert json["prompt"] == "context"
        resp = Mock()
        resp.raise_for_status = Mock()
        resp.json.return_value = {"response": "text"}
        return resp

    monkeypatch.setattr("backend.app.main.requests.post", fake_post)

    resp = client.post("/gen_text", json={"context": "context"})
    assert resp.status_code == 200
    assert resp.json() == {"response": "text"}


def test_list_models(monkeypatch):
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.json.return_value = {"models": [{"name": "foo"}, {"name": "bar"}]}

    def fake_get(url):
        assert "tags" in url
        return mock_resp

    monkeypatch.setattr("backend.app.main.requests.get", fake_get)

    resp = client.get("/list_models")
    assert resp.status_code == 200
    assert resp.json() == {"models": ["foo", "bar"]}


def test_generate_image(monkeypatch):
    monkeypatch.setattr(
        "backend.app.main.ollama_generate_image",
        lambda prompt: {"image": "imgdata"},
    )

    resp = client.post("/gen_image", json={"prompt": "hello"})
    assert resp.status_code == 200
    assert resp.json() == {"image": "imgdata"}
