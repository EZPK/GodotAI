"""Wrapper around the Ollama image generation endpoint."""

from __future__ import annotations

import requests
from .config import settings

OLLAMA_IMAGE_MODEL = settings.ollama_image_model
OLLAMA_IMAGE_HOST = settings.ollama_image_host
OLLAMA_IMAGE_PORT = str(settings.ollama_image_port)
BASE_URL = f"http://{OLLAMA_IMAGE_HOST}:{OLLAMA_IMAGE_PORT}/api"


def generate_image(prompt: str) -> dict:
    """Generate an image using the configured Ollama model."""
    resp = requests.post(
        f"{BASE_URL}/generate-image",
        json={"model": OLLAMA_IMAGE_MODEL, "prompt": prompt},
    )
    resp.raise_for_status()
    return resp.json()
