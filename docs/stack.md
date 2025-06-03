# Stack logiciel

Cette page décrit les principaux composants utilisés dans **GodotAI** et renvoie vers leur documentation officielle.

## FastAPI
Le backend HTTP est construit avec [FastAPI](https://fastapi.tiangolo.com/). Il expose plusieurs routes pour communiquer avec le modèle et stocker les messages.

## Ollama
[Ollama](https://github.com/ollama/ollama) fournit le Large Language Model exécuté dans un conteneur Docker dédié. Les modèles sont téléchargés automatiquement au démarrage.

## Godot
Le client graphique est développé avec [Godot](https://docs.godotengine.org/en/stable/). Des scripts GDScript appellent l'API pour afficher les réponses dans le jeu.

## Docker Compose
L'orchestration des services se fait via [Docker Compose](https://docs.docker.com/compose/). Une simple commande `make up` démarre l'ensemble.

## MkDocs
La documentation vit dans le dossier `docs/` et est construite avec [MkDocs](https://www.mkdocs.org/). Vous pouvez lancer `mkdocs serve` pour un aperçu local.

## Exemple d'appel API
Ci-dessous un petit exemple en Python pour générer du texte via l'API :

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
Un notebook prêt à l'emploi est disponible dans [notebooks/api_example.ipynb](notebooks/api_example.ipynb) pour tester ces appels de manière interactive.
