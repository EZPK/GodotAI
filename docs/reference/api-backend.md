# API du backend

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Vérifie que le backend fonctionne |
| GET | `/txt` | Test de connexion pour la route texte |
| POST | `/txt` | Génère du texte via Ollama |
| GET | `/img` | Retourne une image d'exemple |
| POST | `/img` | Génère une image via Stable Diffusion |
| GET | `/list_models` | Liste les modèles disponibles |
| POST | `/users` | Crée un utilisateur |
| POST | `/sessions` | Crée une session de jeu |
| GET | `/sessions/{id}` | Récupère une session |
| POST | `/mcp` | Endpoint JSON-RPC MCP |


L'API démarre automatiquement avec les autres services :

```bash
make up
```
Cette commande lance Docker Compose qui orchestre les conteneurs FastAPI, Ollama et Stable Diffusion.

## Voir aussi

- [Guide d'utilisation de l'API](../guides/utiliser-api.md)
