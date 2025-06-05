# 🐳 Docker Compose

Docker Compose est l'outil qui lance plusieurs conteneurs Docker en une seule commande.
Le fichier `docker-compose.yml` définit trois services : **fastapi**, **ollama** et **stablediffusion**.

```mermaid
flowchart LR
    DC[Docker Compose] --> F(fastapi)
    DC --> O(ollama)
    DC --> SD(stablediffusion)
    click DC "docker-compose.md" "Voir Docker Compose"
    click F "fastapi.md" "Voir la page FastAPI"
    click O "ollama.md" "Voir la page Ollama"
    click SD "stable-diffusion.md" "Voir la page Stable Diffusion"
```

Pour simplifier la vie du développeur, toutes les commandes utiles sont regroupées dans le `Makefile`.

Commandes utiles :
```bash
# Démarrer les services en arrière-plan
make up

# Arrêter l'ensemble
make down
```

## Voir aussi

- [Fichier `docker-compose.yml`](../reference/docker-compose-yml.md)
- [Makefile](../reference/makefile.md)

## Ressources
- [Site officiel](https://www.docker.com/)
- [Documentation](https://docs.docker.com/compose/)
