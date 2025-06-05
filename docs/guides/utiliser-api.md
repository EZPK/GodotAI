# Utiliser l'API REST

Vous pouvez interagir avec GodotAI sans lancer le client Godot en appelant directement le backend FastAPI.

Exemple d'appel pour générer du texte :
```bash
curl -X POST http://localhost:8000/gen_text \
     -H 'Content-Type: application/json' \
     -d '{"context": "Bonjour"}'
```
La réponse est un objet JSON contenant le texte généré.

## Voir aussi

- [Endpoints détaillés](../reference/api-backend.md)
- [Explications sur FastAPI](../explications/fastapi.md)
