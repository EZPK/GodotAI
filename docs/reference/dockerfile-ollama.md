# 🐋 Dockerfile.ollama

Basé sur l’image officielle `ollama/ollama`, ce Dockerfile ajoute quelques outils pratiques comme `curl` et `pciutils`. Il intègre également le `Modelfile` pour construire le modèle personnalisé `god` et copie le script `entrypoint_ollama.sh` qui gère le téléchargement automatique des modèles.

```
FROM ollama/ollama:latest
RUN apt-get update && apt-get install -y curl pciutils
COPY Modelfile /Modelfile
RUN /bin/ollama create god -f /Modelfile
COPY entrypoint_ollama.sh /entrypoint_ollama.sh
ENTRYPOINT ["/entrypoint_ollama.sh"]
```

Le `Modelfile` est donc empaqueté puis transformé en modèle local grâce à la commande `ollama create god -f /Modelfile`. Ce modèle nommé `god` est ensuite disponible pour l’interface Godot.

L’entrée `ENTRYPOINT` lance ce script pour s’assurer que les modèles précisés sont bien présents avant d’exposer l’API Ollama.

- Les modèles à récupérer sont définis par `OLLAMA_TEXT_MODEL` et `STABLEDIFFUSION_MODEL` dans `docker-compose.yml`.
- Ils sont enregistrés dans le volume Docker `ollama_models` afin d’éviter des téléchargements répétés.

Ce conteneur se combine ensuite avec le service FastAPI via `docker compose up`.

Lancez la stack et la construction de l'image avec `make up`.

## Voir aussi

- [Script `entrypoint_ollama.sh`](entrypoint-ollama.md)
- [Fichier `Modelfile`](modelfile.md)
