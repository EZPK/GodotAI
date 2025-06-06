"""Client helpers for Stable Diffusion image generation."""

from __future__ import annotations

import requests

from .config import settings

IMAGE_BASE_URL = (
    f"http://{settings.STABLEDIFFUSION_HOST}:{settings.STABLEDIFFUSION_PORT}/api"
)


def generate_image(prompt: str) -> dict:
    """Generate an image with the configured Stable Diffusion model."""
    resp = requests.post(
        f"{IMAGE_BASE_URL}/generate-image",
        json={"model": settings.STABLEDIFFUSION_MODEL, "prompt": prompt},
    )
    resp.raise_for_status()
    return resp.json()
