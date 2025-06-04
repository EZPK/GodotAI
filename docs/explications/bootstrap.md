# 🚀 Bootstrap de l'application

Ce schéma retrace les étapes effectuées lors d'un `make up`.

```text
make up
  |
  `- docker compose up
       |
       |-- Construction des images
       |    |- fastapi : Dockerfile -> uvicorn
       |    |- ollama : Dockerfile.ollama -> entrypoint_ollama.sh
       |    `- stablediffusion : image préexistante
       |
       `-- Démarrage des conteneurs
             |
             |-> ollama
             |     `-> entrypoint_ollama.sh
             |          - lance "ollama serve"
             |          - attend que l'API soit prête
             |          - `ollama pull` des modèles manquants
             |
             |-> stablediffusion
             |     - télécharge les poids si nécessaire
             |
             `-> fastapi
                   - exécute uvicorn avec backend_server
```

## Détail des étapes

1. **Commande `make up`** : lance `docker compose up -d` en utilisant les variables
du fichier `.env` pour choisir les ports et les modèles.
2. **Construction des images** : `fastapi` et `ollama` sont (re)construits si nécessaire,
`stablediffusion` est récupérée depuis Docker Hub.
3. **Lancement d'`ollama`** : le script `entrypoint_ollama.sh` démarre
`ollama serve`, vérifie la présence des modèles et les télécharge au besoin.
4. **Lancement de `stablediffusion`** : l'image prévoit un script similaire pour récupérer les poids
avant de démarrer la WebUI.
5. **Lancement de `fastapi`** : une fois les services précédents disponibles, Uvicorn
exécute `backend.app.backend_server:app`.
6. **Application prête** : Godot ou tout autre client peut désormais appeler l'API.
