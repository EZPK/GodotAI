# godot_ai

Ce projet combine un backend FastAPI orchestré avec Docker, un service Ollama pour la génération de texte (LLM), et un client Godot pour l'interface utilisateur. L'ensemble permet de créer des expériences interactives avec des modèles de langage avancés, le tout automatisé et prêt à l'emploi.

## Fonctionnalités principales
- **Backend FastAPI** : Fournit des endpoints pour la génération de texte et d'images, communique avec Ollama via HTTP.
- **Ollama** : Service LLM (ex : llama3:8b, deepseek-coder:14b) lancé dans un conteneur dédié, téléchargement automatique du modèle au démarrage.
- **Godot** : Client graphique, dialogue avec le backend pour afficher les réponses du LLM et les images générées.
- **Orchestration Docker Compose** : Démarrage, arrêt, persistance des modèles, rebuild, etc.
- **Téléchargement automatique du modèle** : Le modèle LLM est téléchargé automatiquement au premier démarrage du conteneur Ollama, avec une barre de progression dans les logs du terminal.

## Structure du projet

- `backend/` : API FastAPI (endpoints texte/image, logique serveur)
- `godot/` : Projet Godot (scènes, scripts, base de données locale)
- `docker-compose.yml` : Orchestration des services (Ollama, backend)
- `Dockerfile.ollama` : Image custom Ollama avec script d'entrée pour gestion du modèle
- `entrypoint_ollama.sh` : Script shell pour téléchargement automatique du modèle
- `Makefile` : Commandes utilitaires pour le développement
- `utils/` : Images statiques, ressources diverses

## Prérequis
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Make](https://www.gnu.org/software/make/)
- [Godot 4.x](https://godotengine.org/) (pour le client)

## Installation et lancement rapide

1. **Cloner le dépôt**

```zsh
git clone <repo_url>
cd godot_ai
```

2. **Lancer les services (Ollama + backend FastAPI)**

```zsh
make up
```

- Le backend FastAPI sera accessible sur http://localhost:8000
- Ollama (LLM) sera accessible sur http://localhost:11434
- Le modèle LLM sera téléchargé automatiquement si besoin (voir logs du conteneur Ollama pour la progression)

3. **Arrêter les services**

```zsh
make down
```

4. **Rebuild complet (si modification Dockerfile, dépendances, etc.)**

```zsh
make rebuild
```

5. **Lancer le client Godot**

Ouvrez le dossier `godot/` avec l'éditeur Godot 4.x et lancez le projet.

## Personnalisation
- Modifiez le modèle LLM utilisé en changeant la variable d'environnement `OLLAMA_TEXT_MODEL` dans `docker-compose.yml`.
- Ajoutez vos endpoints ou scripts dans `backend/app/` ou `godot/scripts/` selon vos besoins.
- Modifiez le `Makefile` pour ajouter des commandes personnalisées.

## Dépannage
- Pour forcer le re-téléchargement du modèle, supprimez le volume Docker associé :
  ```zsh
  docker compose down
  docker volume rm godot_ai_ollama_models
  make up
  ```
- Suivez la progression du téléchargement du modèle dans les logs :
  ```zsh
  docker logs -f ollama
  ```

## Démarrage propre avec téléchargement automatique du modèle

Pour forcer le téléchargement automatique du modèle Ollama (et vérifier la persistance dans le volume Docker) :

1. **Arrêter les services et supprimer le volume de modèles**

```zsh
docker compose down
# Supprime le volume qui contient les modèles Ollama
docker volume rm godot_ai_ollama_models
```

2. **Relancer le service Ollama**

```zsh
docker compose up -d --build ollama
```

3. **Suivre la progression du téléchargement**

```zsh
docker logs -f ollama
```

4. **Vérifier que le modèle est bien disponible**

```zsh
docker exec ollama ollama list
```

5. **Tester l'API Ollama depuis la machine hôte**

```zsh
curl http://localhost:11434/api/tags
```

**Résultat attendu** : le modèle est téléchargé automatiquement au premier démarrage, persiste dans le volume Docker, et l'API Ollama est accessible sur le port 11434 de la machine hôte.

## TODO
- Compléter l'implémentation des endpoints FastAPI dans `backend/app/`
- Ajouter la documentation des endpoints API
- Détailler l'intégration Godot ↔️ backend
- Ajouter la gestion avancée de la progression côté client

---

Pour toute question, ouvrez une issue sur le dépôt.
