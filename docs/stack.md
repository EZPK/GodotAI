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

## Rôle des composants
- **Godot** : interface du jeu et point d'entrée pour le joueur.
- **FastAPI** : serveur Python qui orchestre les échanges et stocke les données dans SQLite.
- **Ollama** : service LLM chargé de générer les réponses textuelles.
- **Stable Diffusion** : moteur de création d'images à partir de vos descriptions.
- **Docker Compose** : outil qui démarre tous les conteneurs d'un coup.
- **MkDocs** : générateur de cette documentation.

## Pages détaillées
- [⚡ FastAPI](fastapi.md)
- [🦙 Ollama](ollama.md)
- [🎨 Stable Diffusion](stable-diffusion.md)
- [🎮 Godot](godot.md)
- [🐳 Docker Compose](docker-compose.md)
- [📚 MkDocs](mkdocs.md)

Chaque page de la documentation renvoie vers le site officiel et le manuel de référence pour en apprendre davantage.

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
