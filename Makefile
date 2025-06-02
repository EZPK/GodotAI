# Makefile 🧙‍♂️ pour gérer le projet RPG LLM Godot avec activation automatique du venv

.DEFAULT_GOAL := help

## 📘 Affiche cette aide
help:
	@echo "\n\033[1;33m🛠 Commandes disponibles :\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m🔹 %-20s\033[0m %s\n", $$1, $$2}'

## 🚢 Lancer les services Docker (Ollama + backend)
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
	godot4 --editor godot/project.godot

## 🧹 Supprime fichiers temporaires / cache
clean:
	@echo "\033[1;31m🗑 Nettoyage des fichiers temporaires...\033[0m"
	rm -rf __pycache__ .pytest_cache */__pycache__ */*/__pycache__ *.pyc *.pyo

# Les commandes venv/install/serve sont supprimées car la gestion Python se fait dans Docker

api_call:
	@echo "🧠  Lancement d’un appel API Godot en mode headless..."
	@~/Téléchargements/Godot_v4.4.1-stable_linux.x86_64 --headless --path godot/ --script scripts/ApiCallHeadless.gd
