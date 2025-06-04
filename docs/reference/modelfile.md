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
