# 🤖 GodotAI

GodotAI permet de piloter un mini-jeu Godot avec un modèle de langage local, le tout orchestré par Docker.

## 🚀 Démarrage rapide
1. Installez [Docker](https://docs.docker.com/get-docker/) et [Git](https://git-scm.com/).
2. Clonez le dépôt :
   ```bash
   git clone <repo_url>
   cd godot_ai
   ```
3. Lancez les services (FastAPI, Ollama et Stable Diffusion) :
   ```bash
   make up
   ```
   Tout tourne alors dans des conteneurs Docker et les modèles sont téléchargés au premier lancement.
   
4. Vérifiez que chaque service répond bien :
   ```bash
   pip install -r backend/requirements.txt
   python utils/test_services.py
   ```
5. (Facultatif) Ouvrez Godot :
   ```bash
   make run-godot
   ```
6. (Facultatif) Exécutez les suites de tests :
   ```bash
   pytest -q
   pytest e2e
   ```
7. Stoppez le tout :
   ```bash
   make down
   ```

L'API répond sur `localhost:8000`.

## 📚 Documentation
Plus d'informations dans le dossier `docs/` ou sur la [documentation en ligne](https://ezpk.github.io/GodotAI).
