# Changer le modèle LLM

Ce guide explique comment utiliser un autre modèle de langage avec GodotAI.

1. Ouvrez `docker-compose.yml` et modifiez la variable `OLLAMA_TEXT_MODEL` pour indiquer le nom du modèle souhaité.
2. Relancez le service Ollama :
   ```bash
   make down
   make up
   ```
   Le nouveau modèle est téléchargé puis chargé automatiquement.
3. Vérifiez la liste des modèles disponibles :
   ```bash
   curl http://localhost:11434/api/tags | jq
   ```
   Vous devriez voir le modèle choisi dans la liste.

## Voir aussi

- [Fichier `docker-compose.yml`](../reference/docker-compose-yml.md)
- [Détails du `Modelfile`](../reference/modelfile.md)
- [Dépannage modèles et GPU](depannage-modeles-gpu.md)

## FAQ

### Pourquoi mon modèle n'est‑il pas téléchargé ?

Assurez‑vous que `OLLAMA_TEXT_MODEL` dans `docker-compose.yml` correspond bien
au modèle souhaité puis exécutez `make down` suivi de `make up`.

### Puis‑je utiliser un modèle non listé ?

Oui, indiquez son nom complet dans `OLLAMA_TEXT_MODEL` tant qu'il est compatible
avec Ollama.
