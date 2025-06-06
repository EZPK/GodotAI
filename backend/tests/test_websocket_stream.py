from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.app.main import app

client = TestClient(app)


async def fake_stream_text(prompt: str):
    yield '{"response": "foo"}'
    yield '{"response": "bar"}'


def test_websocket_stream(monkeypatch):
    monkeypatch.setattr("backend.app.main.ollama_stream_text", fake_stream_text)
    with client.websocket_connect("/ws") as websocket:
        websocket.send_json({"prompt": "hi"})
        first = websocket.receive_text()
        second = websocket.receive_text()
        done = websocket.receive_text()
    assert first == '{"response": "foo"}'
    assert second == '{"response": "bar"}'
    assert done == "[DONE]"
