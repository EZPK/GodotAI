import os
import requests

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")

# Build Ollama base URL from individual variables if available
ollama_host = os.getenv("OLLAMA_TEXT_HOST", "localhost")
ollama_port = os.getenv("OLLAMA_TEXT_PORT", "11434")
OLLAMA_URL = os.getenv("OLLAMA_URL", f"http://{ollama_host}:{ollama_port}")

# Same logic for Stable Diffusion
sd_host = os.getenv("OLLAMA_IMAGE_HOST", "localhost")
sd_port = os.getenv("OLLAMA_IMAGE_PORT", "7860")
SD_URL = os.getenv("SD_URL", f"http://{sd_host}:{sd_port}")


def check_fastapi():
    try:
        r = requests.get(f"{FASTAPI_URL}/")
        r.raise_for_status()
        print("FastAPI OK:", r.json())
        return True
    except Exception as e:
        print("FastAPI error:", e)
        return False


def check_ollama():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags")
        r.raise_for_status()
        print("Ollama OK:", r.json())
        return True
    except Exception as e:
        print("Ollama error:", e)
        return False


def check_stablediffusion():
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models")
        r.raise_for_status()
        print("Stable Diffusion OK")
        return True
    except Exception as e:
        print("Stable Diffusion error:", e)
        return False


if __name__ == "__main__":
    ok_fastapi = check_fastapi()
    ok_ollama = check_ollama()
    ok_sd = check_stablediffusion()
    if ok_fastapi and ok_ollama and ok_sd:
        print("All services reachable")
        exit(0)
    exit(1)
