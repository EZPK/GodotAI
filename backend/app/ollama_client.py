"""Client helpers to query Ollama models."""

from __future__ import annotations

import requests

from .config import settings

TEXT_BASE_URL = f"http://{settings.ollama_text_host}:{settings.ollama_text_port}/api"

IMAGE_BASE_URL = (
    f"http://{settings.STABLEDIFFUSION_HOST}:{settings.STABLEDIFFUSION_PORT}/api"
)



def generate_text(prompt: str) -> dict:
    """Generate text with the configured Ollama model."""
    resp = requests.post(
        f"{TEXT_BASE_URL}/generate",
        json={"model": settings.ollama_text_model, "prompt": prompt},
    )
    resp.raise_for_status()
    return resp.json()
