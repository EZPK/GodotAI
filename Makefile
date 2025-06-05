# Makefile 🧙‍♂️ pour gérer le projet RPG LLM Godot avec activation automatique du venv

.DEFAULT_GOAL := help

ifneq (,$(wildcard .env))
include .env
export
endif

ifndef GODOT_PATH
GODOT_PATH := $(shell command -v godot4 2>/dev/null || echo godot4)
endif
VENV_DIR ?= .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip

help: ## 📘 Affiche cette aide
	@echo "\n\033[1;33m🛠 Commandes disponibles :\033[0m"
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m🔹 %-20s\033[0m %s\n", $$1, $$2}'

up: ## 👍 Lancer tous les services Docker (Ollama, Stable Diffusion et FastAPI)
	docker compose up -d

down: ## 🛑 Arrêter les services Docker
	docker compose down

rebuild: ## 🔄 Rebuild complet des images Docker
	docker compose down
	docker compose build --no-cache
	docker compose up -d

.PHONY: godot

godot: ## 🎮 Lance le projet Godot (modifie selon ton chemin d'accès)
	@echo "\033[1;36m🎮 Ouverture de Godot...\033[0m"
	$(GODOT_PATH) --editor godot/project.godot

run-api: install ## ⚡ Lance l'API FastAPI en local
        @$(PYTHON) -m uvicorn backend.app.main:app --reload

clean: ## 🧹 Supprime fichiers temporaires / cache
	@echo "\033[1;31m🗑 Nettoyage des fichiers temporaires...\033[0m"
	@find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null
	@find . -name '*.py[cod]' -delete 2>/dev/null
	@rm -rf .pytest_cache

cleanall: clean ## 💥 Supprime caches et volumes Docker
	@echo "\033[1;31m🗑 Suppression des volumes Docker...\033[0m"
	docker compose down -v

install: ## 📦 Crée le venv et installe les dépendances
	@test -x $(PYTHON) || python3 -m venv $(VENV_DIR)
	@$(PIP) install --upgrade pip
	@$(PIP) install -r backend/requirements.txt

godot_api_call: ## 🧠 Appel API Godot en mode headless
	@echo "🧠  Lancement d’un appel API Godot en mode headless..."
	$(GODOT_PATH) --headless --path godot/ --script scripts/ApiCallHeadless.gd

generate-diagrams: ## 🖼️ Convertit les fichiers D2 en SVG
	@if command -v d2 >/dev/null 2>&1; then \
		for f in docs/diagrams/*.d2; do \
			d2 "$$f" "docs/assets/$$(basename "$$f" .d2).svg"; \
		done; \
	else \
		echo "Warning: d2 not installed; skipping diagram generation."; \
	fi


docs-serve: install generate-diagrams ## 📚 Lance le serveur MkDocs en local
	@$(PYTHON) -m mkdocs serve

docs-deploy: install generate-diagrams ## 🚀 Déploie la documentation sur GitHub Pages (automatisé via Github Action)
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
	@$(MAKE) generate-diagrams >> rapports/universe.log 2>&1
	@$(PYTHON) -m mkdocs build >> rapports/universe.log 2>&1
	@echo "Logs written to rapports/universe.log"

purge-models: ## 💥 Supprime les modèles téléchargés dans les volumes Docker
	docker compose down
	docker volume rm $$(docker volume ls -qf name=ollama_models) $$(docker volume ls -qf name=sd_models) || true

up-models: ## 🚢 Lance la stack avec MODEL_TEXT et MODEL_IMAGE
	@TEXT=$(or $(MODEL_TEXT),$(OLLAMA_TEXT_MODEL)); \
	IMAGE=$(or $(MODEL_IMAGE),$(OLLAMA_IMAGE_MODEL)); \
	printf '\033[1mMODEL_TEXT:\033[0m %s\n' "$$TEXT"; \
	printf '\033[1mMODEL_IMAGE:\033[0m %s\n' "$$IMAGE"; \
	OLLAMA_TEXT_MODEL=$$TEXT OLLAMA_IMAGE_MODEL=$$IMAGE docker compose up -d
