# 🔧 entrypoint_ollama.sh

Ce script s'exécute lorsque le conteneur Ollama démarre. Son rôle est de préparer l'environnement avant d'exposer l'API.

1. Lancement de `ollama serve` en arrière‑plan.
2. Vérification de la présence des modèles spécifiés dans `OLLAMA_TEXT_MODEL` et `OLLAMA_IMAGE_MODEL`.
3. Téléchargement automatique via `ollama pull` si un modèle manque.
4. Affichage d'une barre de progression pour suivre l'avancement.
5. Attente bloquante tant que `ollama serve` est actif.

Grâce à cette séquence, on dispose d'un service prêt à répondre dès le premier `docker compose up`.
