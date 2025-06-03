# Ce fichier contient le serveur principal FastAPI pour le backend
# TODO: Compléter l'implémentation du backend_server

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import requests
import base64
import os
from fastapi.responses import Response
from sqlalchemy.orm import Session

from . import models
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Backend FastAPI fonctionne !"}


# Modèles de requête
class TextRequest(BaseModel):
    prompt: str


class GenerateTextRequest(BaseModel):
    session_id: int
    action: str


class ImageRequest(BaseModel):
    prompt: str


class GenerateImageRequest(BaseModel):
    description: str
    session_id: int | None = None


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
            json={"model": OLLAMA_TEXT_MODEL, "prompt": req.context},
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint pour générer une image via Ollama
@app.get("/gen_image")
def gen_image_get():
    # Chemin unique, car utils est monté dans /app/utils dans le conteneur Docker
    image_path = "/app/utils/img/image.png"
    try:
        with open(image_path, "rb") as img_file:
            image_bytes = img_file.read()
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur lors de la lecture de l'image : {e}"
        )


@app.post("/gen_image")
def gen_image(req: ImageRequest):
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/generate-image",
            json={"model": OLLAMA_IMAGE_MODEL, "prompt": req.prompt},
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


# --------- Nouveaux endpoints de jeu --------- #


@app.post("/generate-text")
def generate_text(req: GenerateTextRequest, db: Session = Depends(get_db)):
    session = db.query(models.Session).get(req.session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    # Sauvegarde de l'action du joueur
    player_msg = models.Message(
        session_id=req.session_id, sender="player", text=req.action
    )
    db.add(player_msg)
    db.commit()

    last_messages = (
        db.query(models.Message)
        .filter(models.Message.session_id == req.session_id)
        .order_by(models.Message.created_at.desc())
        .limit(5)
        .all()
    )
    context = "\n".join(reversed([m.text for m in last_messages]))

    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/generate",
            json={"model": OLLAMA_TEXT_MODEL, "prompt": context},
        )
        response.raise_for_status()
        data = response.json()
        ai_text = data.get("response", "")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    ai_msg = models.Message(session_id=req.session_id, sender="AI", text=ai_text)
    db.add(ai_msg)
    db.commit()

    return {"text": ai_text}


@app.post("/generate-image")
def generate_image(req: GenerateImageRequest, db: Session = Depends(get_db)):
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/generate-image",
            json={"model": OLLAMA_IMAGE_MODEL, "prompt": req.description},
        )
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if req.session_id is not None:
        img_message = models.Message(
            session_id=req.session_id,
            sender="image",
            text=data.get("image", ""),
        )
        db.add(img_message)
        db.commit()

    return data
