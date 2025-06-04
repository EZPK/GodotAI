# 🛠️ test_services.py

`test_services.py` sert à vérifier que FastAPI, Ollama et Stable Diffusion répondent bien une fois les conteneurs démarrés.

1. Démarrez les services avec `make up`.
2. Installez les dépendances Python si nécessaire :
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Lancez le script :
   ```bash
   python utils/test_services.py
   ```

Ce test est à exécuter juste après `make up` pour vous assurer que la stack est opérationnelle. Il affiche pour chaque service s'il est joignable et renvoie un code de sortie non nul en cas d'échec.
