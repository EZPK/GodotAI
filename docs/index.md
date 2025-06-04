# 🤖 GodotAI

Bienvenue sur la documentation officielle de **GodotAI**. Ce projet combine le moteur de jeu Godot avec un modèle de langage local pour contrôler un mini-jeu. Un serveur FastAPI orchestre les échanges entre Godot, Ollama pour la génération de texte et Stable Diffusion pour les images. Docker Compose relie tous ces services et stocke les données dans SQLite.

Pour aller plus loin, chaque page propose des liens vers le site officiel et la documentation de chaque technologie.

## Déploiement chronologique
1. Installez Docker et Git puis clonez le dépôt.
2. Lancez `make up` pour démarrer Ollama, Stable Diffusion et FastAPI.
3. Patientez pendant le téléchargement automatique des modèles.
4. Vérifiez le bon fonctionnement avec `python utils/test_services.py`.
5. (Optionnel) Ouvrez Godot avec `make run-godot`.
6. (Optionnel) Exécutez les suites de tests `pytest -q` et `pytest e2e`.
7. Arrêtez les services via `make down`.

## Sommaire
- [🚀 Installation](installation.md)
- [🧩 Vue d'ensemble de la stack](stack.md)
  - [⚡ FastAPI](fastapi.md)
  - [📝 Backend détaillé](backend.md)
  - [🦙 Ollama](ollama.md)
  - [🎨 Stable Diffusion](stable-diffusion.md)
  - [🎮 Godot](godot.md)
  - [🐳 Docker Compose](docker-compose.md)
  - [📚 MkDocs](mkdocs.md)
- [📁 Fichiers de configuration](gitignore.md)
  - [`.vale.ini`](vale.md)
  - [`AGENTS.md`](agents-file.md)
  - [`docker-compose.yml`](docker-compose-yml.md)
  - [`Dockerfile.ollama`](dockerfile-ollama.md)
  - [`entrypoint_ollama.sh`](entrypoint-ollama.md)
  - [`Makefile`](makefile.md)
  - [`mkdocs.yml`](mkdocs-yml.md)
- [✅ Tests unitaires](tests-unitaires.md)
- [🚦 Tests E2E](tests-e2e.md)
- [🔧 Vérification des services](test-services.md)
