# ⚡ FastAPI

FastAPI est un framework Web moderne et asynchrone pour Python. Il s'appuie sur
Pydantic pour la validation des données et génère automatiquement une
documentation interactive.

Dans **GodotAI**, FastAPI sert de colonne vertébrale au backend : il expose les
routes appelées par Godot, dialogue avec Ollama pour produire du texte et
déclenche la génération d'images via Stable Diffusion. Il stocke aussi les
informations de partie dans SQLite.

```mermaid
flowchart LR
    G[Godot] --> F(FastAPI)
    F --> O[Ollama]
    F --> SD[Stable Diffusion]
    F --> DB[(SQLite)]
```

## Exemple minimal
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
```

## Ressources
- [Site officiel](https://fastapi.tiangolo.com/)
- [Documentation](https://fastapi.tiangolo.com/)
