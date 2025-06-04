# 🙈 .gitignore

Ce fichier liste tout ce qui doit rester en dehors du suivi Git : les dossiers propres à Godot, les caches Python et les fichiers temporaires. En ignorant ces éléments, on évite d’encombrer le dépôt avec des données générées automatiquement.

Principales entrées :
- `.godot/` et `.import/` pour ne pas versionner les fichiers générés par l’éditeur.
- `__pycache__/` et les fichiers `*.pyc` issus de Python.
- Le dossier `ollama_models` et autres volumes Docker ne sont pas suivis pour préserver l’espace du répertoire Git.

En résumé, `.gitignore` garde le dépôt propre et léger.
