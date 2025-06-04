# 🤖 GodotAI

Bienvenue sur la documentation officielle de **GodotAI**.

Ce projet associe le moteur de jeu Godot à un modèle de langage exécuté localement via Ollama. Un serveur FastAPI orchestre les requêtes et peut déclencher Stable Diffusion pour générer des images. L'ensemble tourne dans des conteneurs Docker et les données sont stockées dans SQLite.

La documentation suit l'approche [Diátaxis](https://diataxis.fr/) afin de séparer
les tutoriels, les guides pratiques, la référence et les explications. Chaque
page renvoie vers les ressources officielles des technologies utilisées.

## Tutoriel : pour commencer 🚀

- [Installation pas à pas](installation.md) : déployez les services et vérifiez qu'ils répondent.
- [Comprendre la stack](stack.md) : découvrez l'architecture et le rôle de chaque composant.

## Référence technique 📁

Cette rubrique décrit les fichiers de configuration du dépôt et les conventions de contribution :
- [AGENTS.md](agents-file.md)
- [docker-compose.yml](docker-compose-yml.md)
- [Makefile](makefile.md)

## Tests et validation ✅

Les pages suivantes expliquent comment vérifier le bon fonctionnement de la stack :
- [Tests unitaires](tests-unitaires.md)
- [Tests E2E](tests-e2e.md)
- [Vérification des services](test-services.md)

Bonne lecture !
