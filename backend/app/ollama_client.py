"""Client helpers to query Ollama models."""

from __future__ import annotations

import requests
import httpx

from .config import settings

TEXT_BASE_URL = f"http://{settings.ollama_text_host}:{settings.ollama_text_port}/api"

IMAGE_BASE_URL = (
    f"http://{settings.STABLEDIFFUSION_HOST}:{settings.STABLEDIFFUSION_PORT}/api"
)


def generate_text(prompt: str, stream: bool = False) -> dict:
    """Generate text with the configured Ollama model."""
    resp = requests.post(
        f"{TEXT_BASE_URL}/generate",
        json={"model": settings.ollama_text_model, "prompt": prompt, "stream": stream},
    )
    resp.raise_for_status()
    return resp.json()


async def stream_text(prompt: str):
    """Stream text tokens from the Ollama model."""
    async with httpx.AsyncClient() as client:
        async with client.stream(
            "POST",
            f"{TEXT_BASE_URL}/generate",
            json={
                "model": settings.ollama_text_model,
                "prompt": prompt,
                "stream": True,
            },
        ) as resp:
            resp.raise_for_status()
            async for line in resp.aiter_lines():
                if line:
                    yield line + "\n"
