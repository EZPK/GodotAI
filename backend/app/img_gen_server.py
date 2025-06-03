"""Wrapper around the Ollama image generation endpoint."""

from __future__ import annotations

import os
import requests

OLLAMA_IMAGE_MODEL = os.environ.get("OLLAMA_IMAGE_MODEL", "llava")
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "ollama")
OLLAMA_PORT = os.environ.get("OLLAMA_PORT", "11434")
BASE_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api"


def generate_image(prompt: str) -> dict:
    """Generate an image using the configured Ollama model."""
    resp = requests.post(
        f"{BASE_URL}/generate-image",
        json={"model": OLLAMA_IMAGE_MODEL, "prompt": prompt},
    )
    resp.raise_for_status()
    return resp.json()
