# Configuration système

Principales variables d'environnement :

- `OLLAMA_TEXT_HOST` : hôte du service Ollama pour le texte (par défaut `ollama`).
- `OLLAMA_TEXT_PORT` : port d'écoute d'Ollama pour le texte (`11434`).
- `OLLAMA_IMAGE_HOST` : hôte du service de génération d'images (`stablediffusion`).
- `OLLAMA_IMAGE_PORT` : port du service d'images (`7860`).
- `OLLAMA_TEXT_MODEL` : modèle utilisé pour la génération de texte.
- `OLLAMA_IMAGE_MODEL` : modèle pour la génération d'images.
- `NVIDIA_VISIBLE_DEVICES` : permet d'activer le GPU dans les conteneurs.

Fichiers importants :

- [`docker-compose.yml`](docker-compose-yml.md) orchestre les services.
- [`Modelfile`](modelfile.md) décrit le modèle et le prompt système.
- [`Dockerfile.ollama`](dockerfile-ollama.md) construit l'image Ollama personnalisée.


Après toute modification, redémarrez la stack via `make down` puis `make up` pour appliquer les nouvelles valeurs.

## Voir aussi

- [Changer le modèle LLM](../guides/changer-modele.md)
