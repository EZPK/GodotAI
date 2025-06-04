# 🤖 GodotAI

GodotAI permet de piloter un mini-jeu Godot avec un modèle de langage local, le tout orchestré par Docker.

## 🚀 Démarrage rapide
1. Installez [Docker](https://docs.docker.com/get-docker/) et [Git](https://git-scm.com/).
2. Clonez le dépôt :
   ```bash
   git clone <repo_url>
   cd godot_ai
   ```
3. Lancez les services :
   ```bash
   make up
   ```
   Les modèles sont téléchargés au premier lancement.
4. (Facultatif) Ouvrez Godot :
   ```bash
   make run-godot
   ```
5. Stoppez le tout :
   ```bash
   make down
   ```

L'API répond sur `localhost:8000`.

## 📚 Documentation
Plus d'informations dans le dossier `docs/` ou sur la [documentation en ligne](https://example.github.io/godot_ai).
