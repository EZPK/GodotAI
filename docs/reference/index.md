# Référence technique

Cette section recense les fichiers essentiels du dépôt et la façon de les utiliser.

## Fichiers principaux

- [`docker-compose.yml`](docker-compose-yml.md) : orchestre FastAPI, Ollama et Stable Diffusion.
- [`Dockerfile.fastapi`](dockerfile.md) : construit l'image du backend FastAPI.
- [`Dockerfile.ollama`](dockerfile-ollama.md) : prépare le service Ollama et lance `entrypoint_ollama.sh`.
- [`Modelfile`](modelfile.md) : définit le prompt système et les paramètres du modèle.
- [`Makefile`](makefile.md) : rassemble les commandes (`make up`, `make down`, `make docs-serve`...).
- [`mkdocs.yml`](mkdocs-yml.md) : configure la documentation.
- [`variables-env.md`](variables-env.md) : liste complète des variables d'environnement.
- [`AGENTS.md`](agents-file.md) : décrit les conventions de contribution automatiques.

## Tests

- [`backend/tests/`](tests-unitaires.md) contient les tests unitaires exécutés avec `pytest`.
- [`e2e/`](tests-e2e.md) stocke un exemple de test Playwright.
- [`utils/test_services.py`](test-services.md) vérifie que les conteneurs répondent correctement.
