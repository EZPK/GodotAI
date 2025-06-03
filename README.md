# godot_ai

Ce projet combine un backend FastAPI orchestré avec Docker, un service Ollama pour la génération de texte (LLM), et un client Godot pour l'interface utilisateur. L'ensemble permet de créer des expériences interactives avec des modèles de langage avancés, le tout automatisé et prêt à l'emploi.

## Fonctionnalités principales
- **Backend FastAPI** : Fournit des endpoints pour la génération de texte et d'images, communique avec Ollama via HTTP.
- **Support du Model Context Protocol (MCP)** : Endpoint `/mcp` compatible JSON-RPC pour initialiser un client et lister prompts, ressources et outils disponibles.
- **Ollama** : Service LLM (ex : llama2, tinyllama) lancé dans un conteneur dédié, téléchargement automatique du modèle au démarrage, support GPU NVIDIA.
- **Godot** : Client graphique, dialogue avec le backend pour afficher les réponses du LLM.
- **Orchestration Docker Compose** : Démarrage, arrêt, persistance des modèles, rebuild, etc.
- **Téléchargement automatique du modèle** : Le modèle LLM est téléchargé automatiquement au premier démarrage du conteneur Ollama, avec une barre de progression dans les logs du terminal.

## Structure du projet
- `backend/` : API FastAPI (endpoints texte/image, logique serveur)
- `godot/` : Projet Godot (scènes, scripts)
- `docker-compose.yml` : Orchestration des services (Ollama, backend) avec support GPU et limitation CPU
- `Dockerfile.ollama` : Image custom Ollama avec script d'entrée pour gestion du modèle
- `entrypoint_ollama.sh` : Script shell pour téléchargement automatique du modèle
- `Modelfile` : Configuration custom du modèle Ollama (paramètres, prompt système)
- `Makefile` : Commandes utilitaires pour le développement

## Prérequis
- [Docker](https://www.docker.com/) + [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) pour le support GPU
- [Docker Compose](https://docs.docker.com/compose/)
- [Make](https://www.gnu.org/software/make/)
- [Godot 4.x](https://godotengine.org/) (pour le client)
- Drivers NVIDIA à jour si usage GPU

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

- Ollama (LLM) sera accessible sur http://localhost:11434
- Le modèle LLM sera téléchargé automatiquement si besoin (voir logs du conteneur Ollama pour la progression)
- Le GPU NVIDIA sera utilisé si disponible (voir logs pour confirmation)

3. **Arrêter les services**

```zsh
make down
```

4. **Rebuild complet (si modification Dockerfile, dépendances, etc.)**

```zsh
make rebuild
```

5. **Lancer le client Godot**

```zsh
make run-godot
```

Ou directement :
```zsh
~/Téléchargements/Godot_v4.4.1-stable_linux.x86_64 --editor godot/project.godot
```

6. **Appel API de test en mode headless**

```zsh
make api_call
```

## Utilisation du Model Context Protocol
Un endpoint `/mcp` répond au format JSON-RPC 2.0.
Les principales méthodes disponibles sont :

- `initialize` : négocie la version du protocole et renvoie les capacités du serveur.
- `prompts/list` : obtient la liste des prompts fournis.
- `resources/list` : renvoie les ressources disponibles.
- `tools/list` : liste les outils exposés par le serveur.

Ces méthodes facilitent l'intégration d'applications agentiques compatibles MCP.

## Personnalisation
- Modifiez le modèle LLM utilisé en changeant la variable d'environnement `OLLAMA_TEXT_MODEL` dans `docker-compose.yml` ou le `Modelfile`.
- Modifiez le prompt système ou les paramètres du modèle dans `Modelfile` (ex : température, contexte, consigne système).
- Ajoutez vos endpoints ou scripts dans `backend/app/` ou `godot/scripts/` selon vos besoins.

## Dépannage & GPU
- Pour forcer le re-téléchargement du modèle, supprimez le volume Docker associé :
  ```zsh
  docker compose down
  docker volume rm godot_ai_ollama_models
  make up
  ```
- Pour vérifier l'utilisation du GPU par Ollama :
  ```zsh
  docker compose logs -f ollama | grep -i gpu
  # ou
  docker exec -it ollama nvidia-smi
  ```
- Pour augmenter les ressources CPU/GPU allouées à Ollama, modifiez les sections `cpus` et `devices` dans `docker-compose.yml`.

## Extrait de configuration Docker Compose (GPU + CPU)
```yaml
services:
  ollama:
    build:
      context: .
      dockerfile: Dockerfile.ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_models:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_TEXT_MODEL=llama2
      - NVIDIA_VISIBLE_DEVICES=all
    restart: unless-stopped
    devices:
      - /dev/nvidiactl:/dev/nvidiactl
      - /dev/nvidia-uvm:/dev/nvidia-uvm
      - /dev/nvidia0:/dev/nvidia0
    cpus: 8.0

volumes:
  ollama_models:
```

## Extrait de Modelfile
```Dockerfile
FROM llama2
PARAMETER temperature 1
PARAMETER num_ctx 1000
SYSTEM TU réponds en français, pas plus de 10 mots
```

## Conseils de performance
- Utilisez un modèle plus petit (`tinyllama`, `phi3:mini`) pour des réponses plus rapides.
- Limitez le nombre de tokens générés (`num_predict` dans la requête API).
- Vérifiez que le GPU est bien utilisé (voir logs).
- Le premier appel est toujours plus lent (chargement du modèle en RAM).

---

Pour toute question, ouvrez une issue sur le dépôt ou consultez les logs Docker pour le debug détaillé.
