# 🎨 Stable Diffusion

Stable Diffusion est un modèle de génération d'images à partir d'une description textuelle.
Dans ce projet, il s'exécute dans un conteneur dédié.

FastAPI lui transmet vos invites afin d'illustrer certaines scènes du jeu.

Vous pouvez générer une image directement via l'API :
```bash
curl -X POST http://localhost:8000/generate-image \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "un village médiéval"}' -o output.png
```

## Ressources
- [Site officiel](https://stability.ai/)
- [Documentation](https://github.com/Stability-AI/stablediffusion)
