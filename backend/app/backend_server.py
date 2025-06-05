# Ce fichier contient le serveur principal FastAPI pour le backend
# TODO: Compléter l'implémentation du backend_server

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import requests
import base64
import os
from fastapi.responses import Response
from sqlalchemy.orm import Session
from datetime import datetime

from .embedding_context import EmbeddingContext
from .img_gen_server import generate_image as ollama_generate_image
from .mcp import router as mcp_router
from .mongo_database import get_mongo_db

from . import models
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(mcp_router)

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


class PromptRequest(BaseModel):
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
from .config import settings

OLLAMA_TEXT_MODEL = settings.ollama_text_model
OLLAMA_IMAGE_MODEL = settings.ollama_image_model

OLLAMA_TEXT_HOST = settings.ollama_text_host
OLLAMA_TEXT_PORT = str(settings.ollama_text_port)
OLLAMA_IMAGE_HOST = settings.ollama_image_host
OLLAMA_IMAGE_PORT = str(settings.ollama_image_port)

OLLAMA_TEXT_BASE_URL = f"http://{OLLAMA_TEXT_HOST}:{OLLAMA_TEXT_PORT}/api"
OLLAMA_IMAGE_BASE_URL = f"http://{OLLAMA_IMAGE_HOST}:{OLLAMA_IMAGE_PORT}/api"


# Endpoint pour générer du texte via Ollama
@app.get("/gen_text")
def gen_text_get():
    return {"text": "hello world"}


@app.post("/gen_text")
def gen_text(req: ContextRequest):
    try:
        response = requests.post(
            f"{OLLAMA_TEXT_BASE_URL}/generate",
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


# --- Simple endpoints for direct model access --- #


@app.post("/text")
def text_model(req: PromptRequest):
    """Generate text using the Ollama container."""
    try:
        resp = requests.post(
            f"{OLLAMA_TEXT_BASE_URL}/generate",
            json={"model": OLLAMA_TEXT_MODEL, "prompt": req.prompt},
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/image")
def image_model(req: PromptRequest):
    """Generate an image using the Stable Diffusion container."""
    try:
        return ollama_generate_image(req.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/list_models")
def list_models():
    try:
        response = requests.get(f"{OLLAMA_TEXT_BASE_URL}/tags")
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
            f"{OLLAMA_TEXT_BASE_URL}/generate",
            json={"model": OLLAMA_TEXT_MODEL, "prompt": context},
        )
        response.raise_for_status()
        data = response.json()
        ai_text = data.get("response", "")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    mongo_db = get_mongo_db()
    mongo_db.llm_logs.insert_one(
        {
            "session_id": req.session_id,
            "prompt": req.action,
            "response": data,
            "timestamp": datetime.utcnow(),
        }
    )

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
