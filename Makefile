# Makefile 🧙‍♂️ pour gérer le projet RPG LLM Godot avec activation automatique du venv

# Empêche make d'afficher "on entre/quitte le répertoire"
MAKEFLAGS += --no-print-directory

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
	@echo "🛠 Commandes disponibles :"
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "🔹 %-20s %s\n", $$1, $$2}'

up: ## 👍 Lancer tous les services Docker (Ollama, Stable Diffusion et FastAPI)
	@echo "🚀 Starting Docker services in background..."
	@docker compose up -d >/dev/null &
	@echo " 🪄 Pour vérifier si un modèle est en train d'être téléchargé, vous pouvez utiliser `docker compose logs -f ollama`"

down: ## 🛑 Arrêter les services Docker
	docker compose down

rebuild: ## 🔄 Rebuild complet des images Docker
	docker compose down
	docker compose build --no-cache
	docker compose up -d

.PHONY: godot

godot: ## 🎮 Lance le projet Godot (modifie selon ton chemin d'accès)
	@echo "🎮 Ouverture de Godot..."
	$(GODOT_PATH) --editor godot/project.godot

run-api: install ## ⚡ Lance l'API FastAPI en local
	@echo "⚡ Starting FastAPI..."
	@$(PYTHON) -m uvicorn backend.app.main:app --reload --log-level warning

clean: ## 🧹 Supprime fichiers temporaires / cache
	@echo "🗑 Nettoyage des fichiers temporaires..."
	@find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name '*.py[cod]' -delete 2>/dev/null || true
	@rm -rf .pytest_cache

cleanall: clean ## 💥 Supprime caches, volumes Docker et le venv
	@echo "🗑 Suppression des volumes Docker..."
	docker compose down -v
	@echo "🗑 Suppression du venv Python..."
	@if [ -n "$$VIRTUAL_ENV" ]; then deactivate; fi; \
	rm -rf $(VENV_DIR)

install: ## 📦 Crée le venv et installe les dépendances
	@test -x $(PYTHON) || python3 -m venv $(VENV_DIR)
	@echo "📦 Installing Python dependencies..."
	@$(PIP) install --upgrade pip -q
	@$(PIP) install -q -r backend/requirements.txt
	@echo "✅ Pour activer le venv : source .venv/bin/activate"

godot_api_call: ## 🧠 Appel API Godot en mode headless
	@echo "🧠  Lancement d’un appel API Godot en mode headless..."
	$(GODOT_PATH) --headless --path godot/ --script scripts/ChatUI.gd

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
	@echo "🪐 Launching full test suite..."
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
	@echo "✅ Logs written to rapports/universe.log"

purge-models: ## 💥 Supprime les modèles téléchargés dans les volumes Docker
	docker compose down
	docker volume rm $$(docker volume ls -qf name=ollama_models) $$(docker volume ls -qf name=sd_models) || true

up-models: ## 🚢 Lance la stack avec MODEL_TEXT et MODEL_IMAGE
	@TEXT=$(or $(MODEL_TEXT),$(OLLAMA_TEXT_MODEL)); \
	IMAGE=$(or $(MODEL_IMAGE),$(STABLEDIFFUSION_MODEL)); \
	printf 'MODEL_TEXT: %s\n' "$$TEXT"; \
	printf 'MODEL_IMAGE: %s\n' "$$IMAGE"; \
	OLLAMA_TEXT_MODEL=$$TEXT STABLEDIFFUSION_MODEL=$$IMAGE docker compose up -d

modeldl:
	@docker logs -f ollama | grep --line-buffered -E 'Pulling|[0-9]{1,3}%'
