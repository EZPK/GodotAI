# 🦙 Ollama

Ollama lance le modèle de langage à l'intérieur d'un conteneur Docker. Il télécharge
le modèle choisi lors du premier démarrage (par exemple Mistral ou Llama 3).
Ce téléchargement s'effectue automatiquement lorsque vous exécutez `make up` et
le modèle reste ensuite disponible localement pour les démarrages suivants.

Le fichier `Modelfile` à la racine du dépôt indique quel modèle charger. FastAPI
lui envoie les requêtes de l'utilisateur pour obtenir une réponse adaptée à la
partie en cours.

Exemple d'exécution manuelle :
```bash
docker run -p 11434:11434 ollama/ollama:latest serve
```

## Ressources
- [Site officiel](https://ollama.ai/)
- [Documentation](https://ollama.ai/docs)
