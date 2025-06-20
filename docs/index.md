# 🤖 GodotAI

Bienvenue sur la documentation officielle de **GodotAI**.

Ce projet associe Godot, FastAPI et Ollama pour proposer un mini-jeu capable de communiquer avec un modèle de langage local. Toute la stack s'exécute dans des conteneurs Docker afin de rester simple à lancer.

🌟 [Retrouvez le dépôt sur GitHub](https://github.com/EZPK/GodotAI/) pour explorer le code source.

## Aperçu de l'architecture

Voici le fonctionnement général : le joueur dialogue avec **Godot**, qui fait
appel au backend **FastAPI**. Celui-ci interroge **Ollama** pour le texte et
**Stable Diffusion** pour l'image, puis consigne les échanges dans **SQLite**
avant de répondre au client.

![Architecture](assets/architecture.svg)

Cette documentation suit le cadre [Diátaxis](https://diataxis.fr/) et se divise en quatre sections :

- **Tutoriels** 🛠️ : apprenez pas à pas à installer et utiliser le projet.
- **Guides pratiques** 🧰 : répondez à un besoin précis après l'installation.
- **Référence** 📚 : trouvez la description exhaustive des commandes et fichiers.
- **Explications** 🧩 : comprenez l'architecture et les choix techniques.

## Accès rapide

- [Tutoriel de prise en main](tutoriels/premiers-pas.md)
- [Guides pratiques](guides/index.md)
- [Référence technique](reference/index.md)
- [Explications](explications/architecture.md)

## Structure détaillée

### 🛠️ Tutoriels
- 🚀 [Prise en main](tutoriels/premiers-pas.md)

### 🧰 Guides pratiques
- 🔄 [Changer le modèle LLM](guides/changer-modele.md)
- ✏️ [Adapter le prompt](guides/adapter-prompt.md)
- 📡 [Utiliser l'API](guides/utiliser-api.md)
- ⚙️ [Configurer l'environnement](guides/configurer-env.md)
- 🩺 [Dépannage modèles et GPU](guides/depannage-modeles-gpu.md)
- ✍️ [Contrôler la rédaction avec Vale](guides/qualite-redaction-vale.md)
- 🛠️ [Troubleshooting](guides/troubleshooting.md)

### 📚 Référence technique
- 🔗 [API du backend](reference/api-backend.md)
- ⚙️ [Configuration](reference/configuration.md)
- 🛠️ [Makefile](reference/makefile.md)
- 🐳 [docker-compose.yml](reference/docker-compose-yml.md)
- 📄 [Dockerfile.fastapi](reference/dockerfile.md)
- ✅ [Tests unitaires](reference/tests-unitaires.md)

### 🧩 Explications
- 🏗️ [Architecture](explications/architecture.md)
- 🗺️ [Flux complet](explications/flux-global.md)
- 🚀 [Bootstrap](explications/bootstrap.md)
- 💻 [Backend détaillé](explications/backend.md)
- ⚡ [FastAPI](explications/fastapi.md)
- 🤖 [Ollama](explications/ollama.md)
- 🎨 [Stable Diffusion](explications/stable-diffusion.md)
- 🎮 [Godot](explications/godot.md)
- 🐋 [Docker Compose](explications/docker-compose.md)
- 📖 [MkDocs](explications/mkdocs.md)

Bonne lecture !
