# 🐳 docker-compose.yml

Ce fichier coordonne les conteneurs nécessaires au projet. Il définit trois services :
- **fastapi** pour le backend Python ;
- **ollama** pour la génération de texte et d’images, construit à partir du `Dockerfile.ollama` ;
- **stablediffusion** pour l’interface Web de Stable Diffusion.

Les volumes comme `ollama_models` et `sd_outputs` conservent les modèles et les résultats entre chaque exécution. Les variables d’environnement proviennent du fichier `.env` afin de personnaliser les ports ou les noms de modèle.

En règle générale, `docker-compose.yml` permet de démarrer l’ensemble avec `docker compose up` ou la commande `make up` prévue dans le projet.

## Voir aussi

- [Guide pour changer de modèle](../guides/changer-modele.md)
- [Explications sur Docker Compose](../explications/docker-compose.md)

## FAQ

### Peut‑on modifier les ports exposés ?

Oui. Mettez à jour les variables correspondantes dans `.env` puis relancez `make up`.

### Comment ajouter un service supplémentaire ?

Déclarez-le dans `docker-compose.yml` et complétez éventuellement le `Makefile`.
