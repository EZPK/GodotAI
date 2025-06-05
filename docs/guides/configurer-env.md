# ⚙️ Configurer l'environnement

Ce guide explique comment personnaliser les variables d'environnement de GodotAI.

1. Ouvrez le fichier `.env` à la racine du dépôt.
2. Modifiez les valeurs selon vos besoins : modèles, ports ou chemin de Godot.
3. Redémarrez la stack pour appliquer les changements :
   ```bash
   make down
   make up
   ```
   La commande téléchargera les modèles définis dans `.env` grâce à `entrypoint_ollama.sh --download` s'ils ne sont pas encore présents.

Pour utiliser le GPU, définissez `NVIDIA_VISIBLE_DEVICES=all` avant de lancer `make up`.

## Voir aussi

- [Liste des variables](../reference/variables-env.md)
