# 🎨 Stable Diffusion

Le service d'images fonctionne grâce à Stable Diffusion. Il s'exécute lui aussi dans un conteneur dédié.

Vous pouvez générer une image directement via l'API :
```bash
curl -X POST http://localhost:8000/generate-image \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "un village médiéval"}' -o output.png
```

- [Dépôt officiel](https://github.com/Stability-AI/stablediffusion)
