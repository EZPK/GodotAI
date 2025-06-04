			# Makefile 🧙‍♂️ pour gérer le projet RPG LLM Godot avec activation automatique du venv

.DEFAULT_GOAL := help

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

GODOT_PATH ?= godot4
VENV_DIR ?= .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip

help: ## 📘 Affiche cette aide
	@echo "\n\033[1;33m🛠 Commandes disponibles :\033[0m"
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m🔹 %-20s\033[0m %s\n", $$1, $$2}'

up: ## 🚢 Lancer tous les services Docker (Ollama, Stable Diffusion et FastAPI)
	docker compose up -d

down: ## 🛑 Arrêter les services Docker
	docker compose down

rebuild: ## 🔄 Rebuild complet des images Docker
	docker compose down
	docker compose build --no-cache
	docker compose up -d

run-godot: ## 🎮 Lance le projet Godot (modifie selon ton chemin d'accès)
	@echo "\033[1;36m🎮 Ouverture de Godot...\033[0m"
	$(GODOT_PATH) --editor godot/project.godot

run-api: install ## ⚡ Lance l'API FastAPI en local
	@$(PYTHON) -m uvicorn backend.app.backend_server:app --reload

clean: ## 🧹 Supprime fichiers temporaires / cache
	@echo "\033[1;31m🗑 Nettoyage des fichiers temporaires...\033[0m"
	rm -rf __pycache__ .pytest_cache */__pycache__ */*/__pycache__ *.pyc *.pyo

install: ## 📦 Crée le venv et installe les dépendances
	@test -x $(PYTHON) || python3 -m venv $(VENV_DIR)
	@$(PIP) install --upgrade pip
	@$(PIP) install -r backend/requirements.txt
	@$(PIP) install black pytest mkdocs mkdocs-material

api_call: ## 🧠 Appel API Godot en mode headless
	@echo "🧠  Lancement d’un appel API Godot en mode headless..."
	$(GODOT_PATH) --headless --path godot/ --script scripts/ApiCallHeadless.gd

docs-serve: install ## 📚 Lance le serveur MkDocs en local
	@$(PYTHON) -m mkdocs serve

docs-deploy: install ## 🚀 Déploie la documentation sur GitHub Pages
	@$(PYTHON) -m mkdocs gh-deploy --clean

universe: install ## 🪐 Lance tous les tests et génère un log complet
	@mkdir -p rapports
	@echo "Running black" > rapports/universe.log
	@$(PYTHON) -m black backend/app >> rapports/universe.log 2>&1
	@echo "\nRunning unit tests" >> rapports/universe.log
	@$(PYTHON) -m pytest -q >> rapports/universe.log 2>&1
	@echo "\nChecking services" >> rapports/universe.log
	@$(PYTHON) utils/test_services.py >> rapports/universe.log 2>&1 || true
	@echo "\nRunning e2e tests" >> rapports/universe.log
	@$(PYTHON) -m pytest e2e/test_api_playwright.py -q >> rapports/universe.log 2>&1 || true
	@echo "\nBuilding docs" >> rapports/universe.log
	@$(PYTHON) -m mkdocs build >> rapports/universe.log 2>&1
	@echo "Logs written to rapports/universe.log"
