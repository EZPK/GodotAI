# 🔧 entrypoint_ollama.sh

Ce script est lancé dans l’image Ollama. Il démarre le serveur puis vérifie que les modèles demandés sont présents. Si besoin, `ollama pull` les télécharge et affiche une barre de progression.

Cette approche garantit qu’un modèle manquant n’empêchera pas le service de démarrer. Une fois les téléchargements terminés, le script attend simplement que `ollama serve` se termine.
