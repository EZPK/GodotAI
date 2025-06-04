# 🚀 Installation pas à pas

1. Installez [Docker](https://docs.docker.com/get-docker/) et [Git](https://git-scm.com/).
2. Clonez le dépôt :
   ```bash
   git clone <repo_url>
   cd godot_ai
   ```
3. Démarrez les services :
   ```bash
   make up
   ```
   Les modèles Ollama se téléchargent automatiquement.
4. (Optionnel) Lancez Godot :
   ```bash
   make run-godot
   ```
5. Coupez les conteneurs :
   ```bash
   make down
   ```
