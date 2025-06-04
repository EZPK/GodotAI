# 🛠️ test_services.py

`test_services.py` sert à vérifier que FastAPI, Ollama et Stable Diffusion répondent bien une fois les conteneurs démarrés.

1. Démarrez les services avec `make up`.
2. Installez les dépendances Python si nécessaire :
   ```bash
   make install
   ```
3. Lancez le script :
   ```bash
   .venv/bin/python utils/test_services.py
   ```

Ce test est à exécuter juste après `make up` pour vous assurer que la stack est opérationnelle. Il affiche pour chaque service s'il est joignable. Un emoji indique l'état : `✅` si tout fonctionne, `⏳` lorsque Stable Diffusion charge encore son modèle et `❌` en cas d'erreur. Le script renvoie un code de sortie non nul si un service est indisponible.
