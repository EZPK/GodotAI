# Ce fichier contient le serveur principal FastAPI pour le backend
# TODO: Compléter l'implémentation du backend_server

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import base64
import os
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend FastAPI fonctionne !"}

# Modèles de requête
class TextRequest(BaseModel):
    prompt: str

class ImageRequest(BaseModel):
    prompt: str

class ContextRequest(BaseModel):
    context: str

# Utilitaire pour choisir le modèle Ollama
OLLAMA_TEXT_MODEL = os.environ.get("OLLAMA_TEXT_MODEL", "llama2")
OLLAMA_IMAGE_MODEL = os.environ.get("OLLAMA_IMAGE_MODEL", "llava")
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "ollama")
OLLAMA_PORT = os.environ.get("OLLAMA_PORT", "11434")
OLLAMA_BASE_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api"

# Endpoint pour générer du texte via Ollama
@app.get("/gen_text")
def gen_text_get():
    return {"text": "hello world"}

@app.post("/gen_text")
def gen_text(req: ContextRequest):
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/generate",
            json={"model": OLLAMA_TEXT_MODEL, "prompt": req.context}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint pour générer une image via Ollama
@app.get("/gen_image")
def gen_image_get():
    # Chemin unique, car utils est monté dans /app/utils dans le conteneur Docker
    image_path = '/app/utils/img/image.png'
    try:
        with open(image_path, "rb") as img_file:
            image_bytes = img_file.read()
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la lecture de l'image : {e}")

@app.post("/gen_image")
def gen_image(req: ImageRequest):
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/generate-image",
            json={"model": OLLAMA_IMAGE_MODEL, "prompt": req.prompt}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/list_models")
def list_models():
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/tags")
        response.raise_for_status()
        data = response.json()
        # Retourne la liste des modèles installés
        return {"models": [m["name"] for m in data.get("models", [])]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
