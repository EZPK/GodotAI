# 🐳 docker-compose.yml

Ce fichier coordonne les conteneurs nécessaires au projet. Il définit cinq services :
- **fastapi** pour le backend Python ;
- **ollama** pour la génération de texte et d’images, construit à partir du `Dockerfile.ollama` ;
- **stablediffusion** pour l’interface Web de Stable Diffusion ;
- **postgres** pour la base relationnelle ;
- **mongo** pour stocker les réponses complètes.
Les volumes nommés, comme `ollama_models`, `sd_models` ou `postgres_data`, conservent les données entre chaque exécution. Les variables sont définies dans `.env`.
En règle générale, `docker-compose.yml` permet de démarrer l’ensemble avec `docker compose up` ou la commande `make up` prévue dans le projet.

## Voir aussi

- [Guide pour changer de modèle](../guides/changer-modele.md)
- [Explications sur Docker Compose](../explications/docker-compose.md)

## FAQ

### Peut‑on modifier les ports exposés ?

Oui. Mettez à jour les variables correspondantes dans `.env` puis relancez `make up`.

### Comment ajouter un service supplémentaire ?

Déclarez-le dans `docker-compose.yml` et complétez éventuellement le `Makefile`.
