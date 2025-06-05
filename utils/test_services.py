import os
import requests

EMO_SUCCESS = "✅"
EMO_ERROR = "❌"
EMO_WAIT = "⏳"

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")

# Build Ollama base URL from individual variables if available
ollama_host = os.getenv("OLLAMA_TEXT_HOST", "localhost")
ollama_port = os.getenv("OLLAMA_TEXT_PORT", "11434")
OLLAMA_URL = os.getenv("OLLAMA_URL", f"http://{ollama_host}:{ollama_port}")

# Same logic for Stable Diffusion
sd_host = os.getenv("STABLEDIFFUSION_HOST", "localhost")
sd_port = os.getenv("STABLEDIFFUSION_PORT", "7860")
SD_URL = os.getenv("SD_URL", f"http://{sd_host}:{sd_port}")


def check_fastapi():
    try:
        r = requests.get(f"{FASTAPI_URL}/")
        r.raise_for_status()
        print(f"FastAPI {EMO_SUCCESS}", r.json())
        return True
    except Exception as e:
        print(f"FastAPI {EMO_ERROR}", e)
        return False


def check_ollama():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags")
        r.raise_for_status()
        print(f"Ollama {EMO_SUCCESS}", r.json())
        return True
    except Exception as e:
        print(f"Ollama {EMO_ERROR}", e)
        return False


def check_stablediffusion():
    try:
        r = requests.get(f"{SD_URL}/sdapi/v1/sd-models")
        r.raise_for_status()
        print(f"Stable Diffusion {EMO_SUCCESS}")
        return True
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            print(f"Stable Diffusion {EMO_WAIT} model loading")
        else:
            print(f"Stable Diffusion {EMO_ERROR}", e)
        return False
    except Exception as e:
        print(f"Stable Diffusion {EMO_ERROR}", e)
        return False


if __name__ == "__main__":
    ok_fastapi = check_fastapi()
    ok_ollama = check_ollama()
    ok_sd = check_stablediffusion()
    if ok_fastapi and ok_ollama and ok_sd:
        print("All services reachable")
        exit(0)
    exit(1)
