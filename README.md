# 🤖 GodotAI

GodotAI combine plusieurs briques pour créer une expérience de jeu pilotée par un LLM. ✨ Ce README récapitule chaque composant et explique comment lancer le projet.

## 🧩 Composants

### 1. ⚡ FastAPI
- Sert d'API REST.
- Expose des routes pour générer du texte et des images via Ollama.
- Implémente le Model Context Protocol (MCP) pour décrire prompts, outils et ressources.
- Stocke utilisateurs, sessions et messages avec SQLAlchemy dans `game.db`.
- Conserve un contexte récent en mémoire grâce à `EmbeddingContext`.

### 2. 🦙 Ollama
- Service LLM exécuté dans un conteneur dédié.
- Le Dockerfile personnalise l'image officielle et lance `entrypoint_ollama.sh` pour télécharger automatiquement le modèle choisi (`OLLAMA_TEXT_MODEL`).
- Support GPU via NVIDIA Container Toolkit.
- Les paramètres par défaut du modèle sont définis dans `Modelfile`.

### 3. 🎮 Godot
- Client graphique basé sur Godot 4.
- Les scripts `ChatUI.gd` et `ApiCallHeadless.gd` communiquent avec le backend par HTTP.
- Permet de tester rapidement l'API en mode éditeur ou en ligne de commande.

### 4. 🐳 Docker Compose
- Orchestration des services `ollama`, `ollama_image` et `backend`.
- Monte des volumes `ollama_models` et `ollama_image_models` pour conserver les modèles téléchargés.
- Les variables d'environnement (GPU, nom des modèles, etc.) sont configurables dans `docker-compose.yml`.

### 5. 📚 MkDocs
- La documentation vit dans le dossier `docs/` et peut être servie via `mkdocs serve`.
- Le déploiement sur GitHub Pages est géré par `mkdocs gh-deploy` (voir Makefile).

## 🚀 Lancer le projet
```bash
# 1. cloner le dépôt
$ git clone <repo_url>
$ cd godot_ai

# 2. démarrer Ollama et l'API
$ make up

# 3. ouvrir le client Godot (facultatif)
$ make run-godot
```
- Ollama écoute sur `localhost:11434` et télécharge le modèle au premier démarrage.
- Le backend est disponible sur `localhost:8000` (voir `backend/app/backend_server.py`).

Pour arrêter les services :
```bash
$ make down
```

## 📝 Model Context Protocol
L'endpoint `/mcp` parle JSON-RPC 2.0. Il permet :
- d'initialiser un client (`initialize`),
- de lister prompts, ressources et outils disponibles.

Ceci simplifie l'intégration d'agents compatibles MCP.

## 🎨 Personnalisation
- Changez le modèle via `OLLAMA_TEXT_MODEL` dans `.env` ou `docker-compose.yml`.
- Modifiez le prompt système dans `Modelfile`.
- Ajoutez vos propres routes dans `backend/app` ou scripts dans `godot/`.

## 📚 Documentation
Une doc synthétique est disponible dans `docs/`. Servez-la en local avec :
```bash
mkdocs serve
```
ou déployez-la via :
```bash
mkdocs gh-deploy --clean
```

---

Pour toute question, consultez les logs Docker ou ouvrez une issue sur le dépôt.
