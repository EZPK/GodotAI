# Ce fichier contient le serveur principal FastAPI pour le backend
# TODO: Compléter l'implémentation du backend_server

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import requests
import base64
import os
from fastapi.responses import Response
from sqlalchemy.orm import Session

from .embedding_context import EmbeddingContext
from .img_gen_server import generate_image as ollama_generate_image

from . import models
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Global context manager for storing recent messages
context_store = EmbeddingContext()


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


class CreateUserRequest(BaseModel):
    username: str


class CreateSessionRequest(BaseModel):
    user_id: int
    scenario: str | None = None


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
        return ollama_generate_image(req.prompt)
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


@app.post("/users")
def create_user(req: CreateUserRequest, db: Session = Depends(get_db)):
    user = models.User(username=req.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"user_id": user.id}


@app.post("/sessions")
def create_session(req: CreateSessionRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).get(req.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    session = models.Session(user_id=req.user_id, scenario=req.scenario)
    db.add(session)
    db.commit()
    db.refresh(session)
    return {"session_id": session.id}


@app.get("/sessions/{session_id}")
def get_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(models.Session).get(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"id": session.id, "user_id": session.user_id, "scenario": session.scenario}


# --------- Nouveaux endpoints de jeu --------- #


@app.post("/generate-text")
def generate_text(req: GenerateTextRequest, db: Session = Depends(get_db)):
    session = db.query(models.Session).get(req.session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    # Save player's action
    player_msg = models.Message(
        session_id=req.session_id, sender="player", text=req.action
    )
    db.add(player_msg)
    db.commit()
    context_store.add_message(req.session_id, req.action)

    context = context_store.get_recent_context(req.session_id)

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
    context_store.add_message(req.session_id, ai_text)

    return {"text": ai_text}


@app.post("/generate-image")
def generate_image(req: GenerateImageRequest, db: Session = Depends(get_db)):
    try:
        data = ollama_generate_image(req.description)
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
        context_store.add_message(req.session_id, data.get("image", ""))

    return data
