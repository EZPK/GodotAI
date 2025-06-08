"""Main FastAPI application for the backend."""

import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import requests
from fastapi.responses import Response
from sqlalchemy.orm import Session
from datetime import datetime
from dotenv import load_dotenv

from .embedding_context import EmbeddingContext
from .ollama_client import generate_text as ollama_generate_text
from .stablediffusion_client import generate_image as stablediffusion_generate_image
from .mcp import router as mcp_router
from .mongo_database import get_mongo_db

from . import models
from .database import Base, engine, get_db

# Charger les variables du .env au runtime
load_dotenv()

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
    stream: bool = False

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

# Récupération des variables d'environnement directement
OLLAMA_TEXT_MODEL = os.getenv("OLLAMA_TEXT_MODEL", "llama2")
STABLEDIFFUSION_MODEL = os.getenv("STABLEDIFFUSION_MODEL", "llava:7b")
OLLAMA_TEXT_HOST = os.getenv("OLLAMA_TEXT_HOST", "ollama")
OLLAMA_TEXT_PORT = os.getenv("OLLAMA_TEXT_PORT", "11434")
STABLEDIFFUSION_HOST = os.getenv("STABLEDIFFUSION_HOST", "stablediffusion")
STABLEDIFFUSION_PORT = os.getenv("STABLEDIFFUSION_PORT", "7860")

OLLAMA_TEXT_BASE_URL = f"http://{OLLAMA_TEXT_HOST}:{OLLAMA_TEXT_PORT}/api"
STABLEDIFFUSION_BASE_URL = f"http://{STABLEDIFFUSION_HOST}:{STABLEDIFFUSION_PORT}/api"

# Example GET endpoints
@app.get("/txt")
def gen_text_get():
    """Simple ping for the text route."""
    return {"text": "hello world"}

@app.get("/img")
def gen_image_get():
    """Return a sample image shipped with the container."""
    image_path = "/app/utils/img/image.png"
    try:
        with open(image_path, "rb") as img_file:
            image_bytes = img_file.read()
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur lors de la lecture de l'image : {e}"
        )

# --- Endpoints calling the Docker services --- #

@app.post("/txt")
def text_model(req: PromptRequest):
    print(req)
    """Generate text using the Ollama container."""
    try:
        return ollama_generate_text(req.prompt, req.stream)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/img")
def image_model(req: PromptRequest):
    """Generate an image using the Stable Diffusion container."""
    try:
        return stablediffusion_generate_image(req.prompt)
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
