# 🐋 Dockerfile.ollama

Basé sur l’image officielle `ollama/ollama`, ce Dockerfile ajoute quelques outils pratiques comme `curl` et `pciutils`. Il copie surtout le script `entrypoint_ollama.sh` qui gère le téléchargement automatique des modèles.

L’entrée `ENTRYPOINT` lance ce script, ce qui permet d’avoir un conteneur immédiatement fonctionnel sans manipulation supplémentaire. On peut ainsi choisir le modèle à charger via la variable `OLLAMA_TEXT_MODEL` définie dans `docker-compose.yml`.
