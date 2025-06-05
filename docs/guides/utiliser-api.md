# Utiliser l'API REST

Vous pouvez interagir avec GodotAI sans lancer le client Godot en appelant directement le backend FastAPI.

Exemple d'appel pour générer du texte :
```bash
curl -X POST http://localhost:8000/txt \
     -H 'Content-Type: application/json' \
     -d '{"prompt": "Bonjour"}'
```
La réponse est un objet JSON contenant le texte généré.

Pour générer directement une image :
```bash
curl -X POST http://localhost:8000/img \
     -H 'Content-Type: application/json' \
     -d '{"prompt": "Un village médiéval"}' -o image.png
```

## Voir aussi

- [Endpoints détaillés](../reference/api-backend.md)
- [Explications sur FastAPI](../explications/fastapi.md)
