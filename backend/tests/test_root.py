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
