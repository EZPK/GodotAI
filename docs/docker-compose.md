# 🐳 Docker Compose

Docker Compose est l'outil qui lance plusieurs conteneurs Docker en une seule commande.
Le fichier `docker-compose.yml` définit trois services : **fastapi**, **ollama** et **stablediffusion**.

Pour simplifier la vie du développeur, toutes les commandes utiles sont regroupées dans le `Makefile`.

Commandes utiles :
```bash
# Démarrer les services en arrière-plan
make up

# Arrêter l'ensemble
make down
```

## Ressources
- [Site officiel](https://www.docker.com/)
- [Documentation](https://docs.docker.com/compose/)
