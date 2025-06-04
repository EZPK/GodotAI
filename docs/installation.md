# 🚀 Installation pas à pas

1. Installez [Docker](https://docs.docker.com/get-docker/) et [Git](https://git-scm.com/).
2. Clonez le dépôt :
   ```bash
   git clone <repo_url>
   cd godot_ai
   ```
3. Démarrez les services :
   ```bash
   make up
   ```
   Les modèles se téléchargent automatiquement au premier démarrage.

   Lors de cette étape, le conteneur **Ollama** récupère le modèle indiqué dans
   le `Modelfile` tandis que **Stable Diffusion** télécharge ses poids si
   nécessaire. Cette opération peut prendre plusieurs minutes mais n'a lieu
   qu'une seule fois.
4. (Optionnel) Lancez Godot :
   ```bash
   make run-godot
   ```
5. Coupez les conteneurs :
   ```bash
   make down
   ```

Tous les outils mentionnés disposent de liens vers leur site officiel et leur documentation sur les pages correspondantes.
