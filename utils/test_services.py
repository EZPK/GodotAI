import os
import requests

FASTAPI_URL = os.environ.get("FASTAPI_URL", "http://localhost:8000")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
SD_URL = os.environ.get("SD_URL", "http://localhost:7860")


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
