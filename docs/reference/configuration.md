# Configuration système

Principales variables d'environnement :

- `OLLAMA_TEXT_HOST` : hôte du service Ollama pour le texte (par défaut `ollama`).
- `OLLAMA_TEXT_PORT` : port d'écoute d'Ollama pour le texte (`11434`).
- `STABLEDIFFUSION_HOST` : hôte du service de génération d'images (`stablediffusion`).
- `STABLEDIFFUSION_PORT` : port du service d'images (`7860`).
- `OLLAMA_TEXT_MODEL` : modèle utilisé pour la génération de texte.
- `STABLEDIFFUSION_MODEL` : modèle pour la génération d'images.
- `NVIDIA_VISIBLE_DEVICES` : permet d'activer le GPU dans les conteneurs.
- `GODOT_PATH` : chemin de l'exécutable Godot.
- `DATABASE_URL` : chaîne de connexion SQL.
- `POSTGRES_USER` et `POSTGRES_PASSWORD` : identifiants PostgreSQL.
- `POSTGRES_DB` : nom de la base PostgreSQL.
- `MONGO_URL` : adresse de MongoDB.
- `MONGO_DB` : base MongoDB utilisée.

Cette liste résume les options principales. Consultez [variables-env.md](variables-env.md) pour le tableau complet.

Fichiers importants :

- [`docker-compose.yml`](docker-compose-yml.md) orchestre les services.
- [`Modelfile`](modelfile.md) décrit le modèle et le prompt système.
- [`Dockerfile.ollama`](dockerfile-ollama.md) construit l'image Ollama personnalisée.

Après toute modification, redémarrez la stack via `make down` puis `make up` pour appliquer les nouvelles valeurs.

## Voir aussi

- [Changer le modèle LLM](../guides/changer-modele.md)
