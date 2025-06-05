# Dépannage des modèles et du GPU

Quelques pistes si les modèles ne se chargent pas ou si le GPU n'est pas utilisé :

- **Forcer le re-téléchargement d'un modèle** :
  ```bash
  docker volume rm godot_ai_ollama_models
  make up
  ```
- **Vérifier l'utilisation du GPU** :
  ```bash
  docker compose logs -f ollama | grep -i gpu
  ```
  ou
  ```bash
  docker exec -it ollama nvidia-smi
  ```

## Voir aussi

- [Changer le modèle LLM](changer-modele.md)
- [Détails de `docker-compose.yml`](../reference/docker-compose-yml.md)
