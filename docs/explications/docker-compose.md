# 🐳 Docker Compose

Docker Compose est l'outil qui lance plusieurs conteneurs Docker en une seule commande.
Le fichier `docker-compose.yml` définit trois services : **fastapi**, **ollama** et **stablediffusion**.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#6200ee','primaryTextColor':'#ffffff','primaryBorderColor':'#6200ee','lineColor':'#6200ee','fontFamily':'Roboto'}}}%%
flowchart LR
    DC[Docker Compose] --> F(fastapi)
    DC --> O(ollama)
    DC --> SD(stablediffusion)
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
