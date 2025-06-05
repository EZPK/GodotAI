import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from backend.app.embedding_context import EmbeddingContext
from backend.app.ollama_client import generate_image

from unittest.mock import Mock


def test_embedding_context_recent_messages():
    ctx = EmbeddingContext(max_messages=3)
    ctx.add_message(1, "msg1")
    ctx.add_message(1, "msg2")
    assert ctx.get_recent_context(1) == "msg1\nmsg2"

    ctx.add_message(1, "msg3")
    ctx.add_message(1, "msg4")
    # should keep only the last 3 messages
    assert ctx.get_recent_context(1) == "msg2\nmsg3\nmsg4"


def test_generate_image(monkeypatch):
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {"image": "data"}

    def fake_post(url, json):
        assert "generate-image" in url
        assert json["prompt"] == "a prompt"
        return mock_response

    monkeypatch.setattr("backend.app.ollama_client.requests.post", fake_post)
    result = generate_image("a prompt")
    assert result == {"image": "data"}
