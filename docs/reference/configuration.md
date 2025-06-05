# Configuration système

Principales variables d'environnement :

- `OLLAMA_HOST` : hôte du service Ollama (par défaut `ollama`).
- `OLLAMA_PORT` : port d'écoute d'Ollama (`11434`).
- `OLLAMA_TEXT_MODEL` : modèle utilisé pour la génération de texte.
- `OLLAMA_IMAGE_MODEL` : modèle pour la génération d'images.
- `NVIDIA_VISIBLE_DEVICES` : permet d'activer le GPU dans le conteneur.

Fichiers importants :

- [`docker-compose.yml`](docker-compose-yml.md) orchestre les services.
- [`Modelfile`](modelfile.md) décrit le modèle et le prompt système.
- [`Dockerfile.ollama`](dockerfile-ollama.md) construit l'image Ollama personnalisée.


Après toute modification, redémarrez la stack via `make down` puis `make up` pour appliquer les nouvelles valeurs.

## Voir aussi

- [Changer le modèle LLM](../guides/changer-modele.md)
