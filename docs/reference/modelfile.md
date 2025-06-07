# 📑 Modelfile

`Modelfile` définit quel modèle Ollama doit charger et le prompt système à appliquer.

Extrait simplifié :
```Dockerfile
FROM mistral:7b-instruct
PARAMETER temperature 0.5
PARAMETER num_ctx 200
SYSTEM """
Tu es un maître du jeu francophone...
"""
```

La directive `FROM` choisit la base du modèle. Les lignes `PARAMETER` ajustent son comportement, par exemple la créativité (`temperature`) ou la taille du contexte (`num_ctx`). Le bloc `SYSTEM` contient le prompt envoyé au modèle à chaque requête.

Ce fichier est copié dans l'image Ollama construite via `Dockerfile.ollama`. En le modifiant, on peut changer de modèle ou personnaliser l'expérience de jeu.

Lors du premier démarrage du conteneur, la commande suivante génère le modèle local :

```bash
ollama serve &
until curl -s http://127.0.0.1:11434/api/tags > /dev/null; do sleep 1; done
ollama create god -f /Modelfile
kill $!
```

## Voir aussi

- [Guide pour adapter le prompt](../guides/adapter-prompt.md)

## FAQ

### Où se trouve ce fichier dans le conteneur ?

Il est intégré à l'image Ollama lors de la construction. Toute modification nécessite donc un redémarrage via `make up` pour être prise en compte.

### Peut‑on utiliser plusieurs Modelfiles ?

`docker-compose.yml` fait référence à un unique `Modelfile`. Pour tester plusieurs prompts, modifiez ce fichier puis redémarrez Ollama avec `make down` puis `make up` pour prendre en compte les changements.
