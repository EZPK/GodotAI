# 🐋 Dockerfile.ollama

Basé sur l’image officielle `ollama/ollama`, ce Dockerfile ajoute quelques outils pratiques comme `curl` et `pciutils`. Il intègre également le `Modelfile` copié dans l'image et le script `entrypoint_ollama.sh` qui gère la création du modèle personnalisé `god` ainsi que le téléchargement automatique des autres modèles.

```
FROM ollama/ollama:latest
RUN apt-get update && apt-get install -y curl pciutils
COPY Modelfile /Modelfile
COPY entrypoint_ollama.sh /entrypoint_ollama.sh
ENTRYPOINT ["/entrypoint_ollama.sh"]
```

Le `Modelfile` est embarqué dans l'image. Lors du premier démarrage, `entrypoint_ollama.sh` utilise ce fichier pour générer le modèle local `god` dans le volume `ollama_models`.

L’entrée `ENTRYPOINT` lance ce script pour s’assurer que les modèles précisés sont bien présents avant d’exposer l’API Ollama.

- Les modèles à récupérer sont définis par `OLLAMA_TEXT_MODEL` et `STABLEDIFFUSION_MODEL` dans `docker-compose.yml`.
- Ils sont enregistrés dans le volume Docker `ollama_models` afin d’éviter des téléchargements répétés.

Ce conteneur se combine ensuite avec le service FastAPI via `docker compose up`.

Lancez la stack et la construction de l'image avec `make up`.

## Voir aussi

- [Script `entrypoint_ollama.sh`](entrypoint-ollama.md)
- [Fichier `Modelfile`](modelfile.md)
