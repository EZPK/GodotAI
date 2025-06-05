# API du backend

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Vérifie que le backend fonctionne |
| POST | `/gen_text` | Génère du texte à partir d'un contexte |
| GET | `/gen_image` | Retourne une image d'exemple |
| POST | `/gen_image` | Génère une image via Ollama |
| POST | `/txt` | Appelle directement Ollama pour générer du texte |
| POST | `/img` | Appelle Stable Diffusion pour générer une image |
| GET | `/list_models` | Liste les modèles disponibles |
| POST | `/users` | Crée un utilisateur |
| POST | `/sessions` | Crée une session de jeu |
| GET | `/sessions/{id}` | Récupère une session |
| POST | `/generate-text` | Génère une réponse dans la session |
| POST | `/generate-image` | Génère une image et l'enregistre |


L'API démarre automatiquement avec les autres services :

```bash
make up
```
Cette commande lance Docker Compose qui orchestre les conteneurs FastAPI, Ollama et Stable Diffusion.

## Voir aussi

- [Guide d'utilisation de l'API](../guides/utiliser-api.md)
