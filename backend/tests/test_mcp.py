from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.app.backend_server import app

client = TestClient(app)


def test_initialize():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "TestClient", "version": "0.0.1"},
        },
    }
    resp = client.post("/mcp", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert data["id"] == 1
    assert "result" in data


def _rpc(method: str):
    return {"jsonrpc": "2.0", "id": 99, "method": method}


def test_prompts_list():
    resp = client.post("/mcp", json=_rpc("prompts/list"))
    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert "prompts" in data["result"]


def test_resources_list():
    resp = client.post("/mcp", json=_rpc("resources/list"))
    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert "resources" in data["result"]


def test_tools_list():
    resp = client.post("/mcp", json=_rpc("tools/list"))
    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert "tools" in data["result"]
