# 📝 Backend détaillé

Cette page explore plus en profondeur les modules Python du dossier `backend/app`.

Le backend utilise **FastAPI** pour exposer plusieurs routes appelées par le
jeu Godot. Lorsqu'une action du joueur est reçue, elle est envoyée à **Ollama**
pour produire une réponse puis, si besoin, à **Stable Diffusion** pour
générer une illustration. Les échanges structurés sont stockés dans SQLite ou
PostgreSQL via SQLAlchemy, tandis que les réponses brutes du modèle sont
archivées dans MongoDB.

## main.py
Ce fichier instancie FastAPI et expose les routes principales du projet. Il gère
la génération de texte avec Ollama et la création d'images via Stable Diffusion.
Il inclut également le routeur `mcp.py` qui implémente un petit protocole
JSON-RPC (un format d'appel distant basé sur JSON).

## mcp.py
Le module `mcp.py` définit un routeur FastAPI dédié au protocole MCP. Il permet
de décrire les outils et ressources mis à disposition par le backend et gère
les requêtes JSON-RPC entrantes.

## models.py et database.py
La persistance s'appuie sur SQLAlchemy avec une base SQLite par défaut ou
PostgreSQL si configuré. Les modèles `User`, `Session` et `Message` décrivent la
structure principale des données du jeu. Les réponses JSON complètes sont
sauvegardées dans MongoDB grâce au module
`mongo_database.py`.

## embedding_context.py
`EmbeddingContext` conserve en mémoire les derniers messages d'une session afin
de fournir un contexte lors des échanges avec le modèle de langage.

## ollama_client.py
Ce module regroupe les appels HTTP nécessaires pour interroger **Ollama** afin
de générer du texte. Il est invoqué par le serveur lorsqu'une réponse
conversationnelle est demandée.

## stablediffusion_client.py
Cette nouvelle unité se charge d'appeler **Stable Diffusion** pour produire les
illustrations. Elle est isolée afin de ne plus mêler la logique de génération
d'images avec celle du texte.

## config.py
Toutes les variables de configuration (hôtes, ports, nom des modèles Ollama)
proviennent de ce fichier. Les valeurs peuvent être surchargées via un fichier
`.env`.

---

En résumé, le backend combine FastAPI, SQLAlchemy et plusieurs services externes
pour orchestrer la partie narrative du mini-jeu Godot. L'ensemble est démarré
par Docker Compose et reste facilement extensible.

## Voir aussi

- [Référence de l'API](../reference/api-backend.md)
- [Explications sur FastAPI](fastapi.md)
