# 🚀 Premiers pas

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
   Les modèles se téléchargent automatiquement au premier démarrage. Utilisez
   `make up-models MODEL_TEXT=mistral:7b MODEL_IMAGE=stable-diffusion` pour
   spécifier d'autres modèles. Les noms sélectionnés s'affichent alors en clair.

   Lors de cette étape, le conteneur **Ollama** récupère le modèle indiqué dans
   le `Modelfile` tandis que **Stable Diffusion** télécharge ses poids si
   nécessaire. Cette opération peut prendre plusieurs minutes mais n'a lieu
   qu'une seule fois.
   Le script `entrypoint_ollama.sh` lance `ollama serve` puis vérifie la
   présence des modèles. S'ils sont absents, il exécute `ollama pull` pour les
   récupérer avant de poursuivre l'initialisation.
4. Installez les dépendances Python puis vérifiez que FastAPI, Ollama et Stable Diffusion répondent :
   ```bash
   make install
   .venv/bin/python utils/test_services.py
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

Une fois ces étapes terminées, vous pouvez explorer les guides pratiques pour personnaliser le projet.
