# 🧩 Comprendre la stack

Cette page présente brièvement l'architecture générale avant de détailler chaque composant.

```text
[Utilisateur]
     |
   Godot 🎮
     |
  FastAPI ⚡
   /   \
Ollama 🦙  Stable Diffusion 🎨
     \
     SQLite 📂
```

## Pages détaillées
- [⚡ FastAPI](fastapi.md)
- [🦙 Ollama](ollama.md)
- [🎨 Stable Diffusion](stable-diffusion.md)
- [🎮 Godot](godot.md)
- [🐳 Docker Compose](docker-compose.md)
- [📚 MkDocs](mkdocs.md)

## Exemple d'appel API
```python
import requests

BASE_URL = "http://localhost:8000"
resp = requests.post(
    f"{BASE_URL}/generate-text",
    json={"session_id": 1, "action": "look around"},
)
print(resp.json())
```

## Notebook Jupyter
Essayez le notebook [notebooks/api_example.ipynb](notebooks/api_example.ipynb) pour tester ces appels interactivement.
