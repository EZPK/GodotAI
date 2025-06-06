import threading
import time

import os
import sys
import uvicorn

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from backend.app.main import app
from playwright.sync_api import sync_playwright


def _start_server():
    uvicorn.run(app, host="127.0.0.1", port=8002, log_level="error")


def test_root_endpoint():
    server = threading.Thread(target=_start_server, daemon=True)
    server.start()
    time.sleep(1)

    with sync_playwright() as p:
        request = p.request.new_context(base_url="http://127.0.0.1:8002")
        resp = request.get("/")
        assert resp.status == 200
        assert resp.json()["message"] == "Backend FastAPI fonctionne !"
