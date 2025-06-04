# 🐳 docker-compose.yml

Ce fichier coordonne les conteneurs nécessaires au projet. Il définit deux services :
- **ollama** pour la génération de texte et d’images, construit à partir du `Dockerfile.ollama` ;
- **stablediffusion** pour l’interface Web de Stable Diffusion.

Les volumes comme `ollama_models` et `sd_outputs` conservent les modèles et les résultats entre chaque exécution. Les variables d’environnement proviennent du fichier `.env` afin de personnaliser les ports ou les noms de modèle.

En règle générale, `docker-compose.yml` permet de démarrer l’ensemble avec `docker compose up` ou la commande `make up` prévue dans le projet.
