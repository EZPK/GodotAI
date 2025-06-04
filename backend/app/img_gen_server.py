"""Wrapper around the Ollama image generation endpoint."""

from __future__ import annotations

import os
import requests

OLLAMA_IMAGE_MODEL = os.environ.get("OLLAMA_IMAGE_MODEL", "llava:7b")
OLLAMA_IMAGE_HOST = os.environ.get("OLLAMA_IMAGE_HOST", "ollama_image")
OLLAMA_IMAGE_PORT = os.environ.get("OLLAMA_IMAGE_PORT", "11435")
BASE_URL = f"http://{OLLAMA_IMAGE_HOST}:{OLLAMA_IMAGE_PORT}/api"


def generate_image(prompt: str) -> dict:
    """Generate an image using the configured Ollama model."""
    resp = requests.post(
        f"{BASE_URL}/generate-image",
        json={"model": OLLAMA_IMAGE_MODEL, "prompt": prompt},
    )
    resp.raise_for_status()
    return resp.json()
