# 🐋 Dockerfile.ollama

Basé sur l’image officielle `ollama/ollama`, ce Dockerfile ajoute quelques outils pratiques comme `curl` et `pciutils`. Il copie surtout le script `entrypoint_ollama.sh` qui gère le téléchargement automatique des modèles.

```
FROM ollama/ollama:latest
RUN apt-get update && apt-get install -y curl pciutils
COPY entrypoint_ollama.sh /entrypoint_ollama.sh
ENTRYPOINT ["/entrypoint_ollama.sh"]
```

L’entrée `ENTRYPOINT` lance ce script pour s’assurer que les modèles précisés sont bien présents avant d’exposer l’API Ollama.

- Les modèles à récupérer sont définis par `OLLAMA_TEXT_MODEL` et `OLLAMA_IMAGE_MODEL` dans `docker-compose.yml`.
- Ils sont enregistrés dans le volume Docker `ollama_models` afin d’éviter des téléchargements répétés.

Ce conteneur se combine ensuite avec le service FastAPI via `docker compose up`.

Lancez la stack et la construction de l'image avec `make up`.
