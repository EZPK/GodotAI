# 🦙 Ollama

Ollama lance le modèle de langage à l'intérieur d'un conteneur Docker. Il télécharge
le modèle choisi lors du premier démarrage (par exemple Mistral ou Llama 3).
Lorsque vous exécutez `make up`, le conteneur lance le script `entrypoint_ollama.sh` qui vérifie la présence des modèles et les télécharge automatiquement s'ils sont absents.

Le processus est piloté par le script `entrypoint_ollama.sh` :
1. Il démarre `ollama serve` en arrière-plan et attend que l'API réponde.
2. Il vérifie la présence des modèles listés dans les variables d'environnement
   `OLLAMA_TEXT_MODEL` et `STABLEDIFFUSION_MODEL` via `ollama list`.
3. Si l'un d'eux est absent, `ollama pull` est exécuté pour le télécharger.
4. Enfin, le script laisse tourner `ollama serve` pour traiter les requêtes.

Les modèles restent dans le volume Docker `ollama_models`, évitant ainsi de
nouveaux téléchargements aux lancements suivants.

Le fichier `Modelfile` à la racine du dépôt indique quel modèle charger. FastAPI
lui envoie les requêtes de l'utilisateur pour obtenir une réponse adaptée à la
partie en cours.

Lors de la construction de l'image, cette configuration est transformée en un modèle nommé `god` via :

```bash
ollama create god -f /Modelfile
```

## Voir aussi

- [Fichier `Modelfile`](../reference/modelfile.md)
- [Changer de modèle](../guides/changer-modele.md)

![Dialogue avec Ollama](../assets/ollama.svg)

Exemple d'exécution manuelle :
```bash
docker run -p 11434:11434 ollama/ollama:latest serve
```

## Ressources
- [Site officiel](https://ollama.ai/)
- [Documentation](https://ollama.ai/docs)
