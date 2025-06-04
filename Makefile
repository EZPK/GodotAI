# Makefile 🧙‍♂️ pour gérer le projet RPG LLM Godot avec activation automatique du venv

.DEFAULT_GOAL := help

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

GODOT_PATH ?= godot4

## 📘 Affiche cette aide
help:
	@echo "\n\033[1;33m🛠 Commandes disponibles :\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m🔹 %-20s\033[0m %s\n", $$1, $$2}'

## 🚢 Lancer tous les services Docker (Ollama, Stable Diffusion et FastAPI)
up:
	docker compose up -d

## 🛑 Arrêter les services Docker
down:
	docker compose down

## 🔄 Rebuild complet des images Docker
rebuild:
	docker compose down
	docker compose build --no-cache
	docker compose up -d

## 🎮 Lance le projet Godot (modifie selon ton chemin d'accès)
run-godot:
	@echo "\033[1;36m🎮 Ouverture de Godot...\033[0m"
	$(GODOT_PATH) --editor godot/project.godot

## ⚡ Lance l'API FastAPI en local
run-api:
	@uvicorn backend.app.backend_server:app --reload

## 🧹 Supprime fichiers temporaires / cache
clean:
	@echo "\033[1;31m🗑 Nettoyage des fichiers temporaires...\033[0m"
	rm -rf __pycache__ .pytest_cache */__pycache__ */*/__pycache__ *.pyc *.pyo

# Les commandes venv/install/serve sont supprimées car la gestion Python se fait dans Docker

api_call:
	@echo "🧠  Lancement d’un appel API Godot en mode headless..."
	@~/Téléchargements/Godot_v4.4.1-stable_linux.x86_64 --headless --path godot/ --script scripts/ApiCallHeadless.gd

## 📚 Lance le serveur MkDocs en local
docs-serve:
	mkdocs serve

## 🚀 Déploie la documentation sur GitHub Pages
docs-deploy:
	mkdocs gh-deploy --clean

## 🪐 Lance tous les tests et génère un log complet
universe:
	@mkdir -p rapports
	@echo "Running black" > rapports/universe.log
	@black backend/app >> rapports/universe.log 2>&1
	@echo "\nRunning unit tests" >> rapports/universe.log
	@pytest -q >> rapports/universe.log 2>&1
	@echo "\nChecking services" >> rapports/universe.log
	@python utils/test_services.py >> rapports/universe.log 2>&1 || true
	@echo "\nRunning e2e tests" >> rapports/universe.log
	@pytest e2e/test_api_playwright.py -q >> rapports/universe.log 2>&1 || true
	@echo "\nBuilding docs" >> rapports/universe.log
	@mkdocs build >> rapports/universe.log 2>&1
	@echo "Logs written to rapports/universe.log"
