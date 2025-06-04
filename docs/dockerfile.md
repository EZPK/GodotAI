# 🐋 Dockerfile

Le `Dockerfile` construit l'image du backend FastAPI. Basée sur `python:3.11-slim`,
elle installe les dépendances listées dans `backend/requirements.txt` puis copie
le code du dossier `backend`.

Le conteneur lance ensuite Uvicorn sur le port 8000 :
```Dockerfile
CMD ["uvicorn", "backend.app.backend_server:app", "--host", "0.0.0.0", "--port", "8000"]
```
Ce service est ensuite démarré par `docker-compose.yml` sous le nom **fastapi**.
