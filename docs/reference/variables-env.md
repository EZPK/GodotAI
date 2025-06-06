# 🌡️ Variables d'environnement

Le fichier `.env` centralise la configuration de l'ensemble des services. Voici la liste des variables disponibles :

| Variable | Valeur par défaut | Rôle |
|----------|--------------------|-------|
| `OLLAMA_TEXT_MODEL` | `god:latest` | Modèle de génération de texte. |
| `OLLAMA_TEXT_HOST` | `ollama` | Hôte du service Ollama pour le texte. |
| `OLLAMA_TEXT_PORT` | `11434` | Port d'Ollama pour les requêtes texte. |
| `STABLEDIFFUSION_MODEL` | `stable-diffusion` | Modèle de génération d'images. |
| `STABLEDIFFUSION_HOST` | `stablediffusion` | Hôte pour la génération d'images. |
| `STABLEDIFFUSION_PORT` | `7860` | Port du service d'images. |
| `GODOT_PATH` | `./Godot_v4.x86_64` | Exécutable Godot utilisé par le `Makefile`. Si absent, `godot4` est essayé. |
| `DATABASE_URL` | `sqlite:///./data/game.db` | Chaîne de connexion SQL. |
| `POSTGRES_USER` | `postgres` | Utilisateur de la base PostgreSQL. |
| `POSTGRES_PASSWORD` | `postgres` | Mot de passe PostgreSQL. |
| `POSTGRES_DB` | `godotai` | Nom de la base PostgreSQL. |
| `MONGO_URL` | `mongodb://mongo:27017` | Adresse de la base MongoDB. |
| `NVIDIA_VISIBLE_DEVICES` | _(vide)_ | Active l'accélération GPU dans les conteneurs. |

Ces valeurs sont chargées automatiquement par Docker Compose et le `Makefile`.

## Voir aussi

- [Configurer l'environnement](../guides/configurer-env.md)
