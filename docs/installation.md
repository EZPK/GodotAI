# 🚀 Installation pas à pas

Suivez les étapes ci-dessous dans l'ordre pour déployer la stack complète.

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
   Les modèles se téléchargent automatiquement au premier démarrage.

   Lors de cette étape, le conteneur **Ollama** récupère le modèle indiqué dans
   le `Modelfile` tandis que **Stable Diffusion** télécharge ses poids si
   nécessaire. Cette opération peut prendre plusieurs minutes mais n'a lieu
   qu'une seule fois.
   Le script `entrypoint_ollama.sh` lance `ollama serve` puis vérifie la
   présence des modèles. S'ils sont absents, il exécute `ollama pull` pour les
   récupérer avant de poursuivre l'initialisation.
4. Vérifiez que FastAPI, Ollama et Stable Diffusion répondent :
   ```bash
   pip install -r backend/requirements.txt
   python utils/test_services.py
   ```
   Ce script s'assure que chaque service est joignable.
5. (Optionnel) Lancez Godot :
   ```bash
   make run-godot
   ```
6. (Optionnel) Exécutez les tests unitaires et E2E :
   ```bash
   pytest -q
   pytest e2e
   ```
7. Coupez les conteneurs :
   ```bash
   make down
   ```

Tous les outils mentionnés disposent de liens vers leur site officiel et leur documentation sur les pages correspondantes.
