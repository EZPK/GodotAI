# Configuration système

Principales variables d'environnement :

- `OLLAMA_HOST` : hôte du service Ollama (par défaut `ollama`).
- `OLLAMA_PORT` : port d'écoute d'Ollama (`11434`).
- `OLLAMA_TEXT_MODEL` : modèle utilisé pour la génération de texte.
- `OLLAMA_IMAGE_MODEL` : modèle pour la génération d'images.
- `NVIDIA_VISIBLE_DEVICES` : permet d'activer le GPU dans le conteneur.

Fichiers importants :

- `docker-compose.yml` orchestre les services.
- `Modelfile` décrit le modèle et le prompt système.
- `Dockerfile.ollama` construit l'image Ollama personnalisée.
