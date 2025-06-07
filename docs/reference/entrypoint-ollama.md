# 🔧 entrypoint_ollama.sh

Ce script s'exécute lorsque le conteneur Ollama démarre. Son rôle est de préparer l'environnement avant d'exposer l'API.

1. Lancement de `ollama serve` en arrière‑plan.
2. Création du modèle local `god` à partir du `Modelfile` si nécessaire.
3. Vérification de la présence des modèles spécifiés dans `OLLAMA_TEXT_MODEL` et `STABLEDIFFUSION_MODEL`.
4. Téléchargement automatique via `ollama pull` si un modèle manque.
5. Affichage d'une barre de progression pour suivre l'avancement.
6. Attente bloquante tant que `ollama serve` est actif.

Grâce à cette séquence, le modèle `god` est stocké dans le volume `ollama_models` et le service est prêt à répondre dès le premier `docker compose up`.

## Voir aussi

- [Dockerfile.ollama](dockerfile-ollama.md)
- [Modelfile](modelfile.md)
