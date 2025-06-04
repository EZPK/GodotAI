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
