# AGENTS.md - Directives pour l'agent

Ce dépôt rassemble un backend **FastAPI** piloté par Docker ainsi qu'un client **Godot**.
L'agent qui contribue ici doit suivre les instructions suivantes :

1. **Tester le code Python**
   - Si une modification touche des fichiers Python (dossier `backend/app`), exécuter `pytest -q` pour vérifier que tout passe, même s'il n'y a pas encore de tests.
   - Ajouter des tests dans `backend/tests` pour toute nouvelle fonctionnalité.

2. **Style de code**
   - Utiliser `black` pour formater le Python.
   - Exemple de commande :
     ```bash
     black backend/app
     ```

3. **Messages de commit**
   - Utiliser l'impératif présent en anglais, par ex. `Add example API endpoint`.

4. **Création de PR**
   - Le message de la pull request doit commencer par l'emoji `🤖`.

Ces consignes s'appliquent à l'ensemble du dépôt.

5. **Documentation**
   - Vérifier que la documentation dans `docs/` et `mkdocs.yml` reste fidèle au fonctionnement actuel du projet.
   - Ajouter tout nouvel article Markdown au sommaire de `mkdocs.yml` et lier la page depuis `docs/index.md`.
   - Les pages doivent détailler la pile technique et expliquer le code de ce dépôt en profondeur.
   - Après chaque mise à jour de la documentation, exécuter `mkdocs build` pour s'assurer que le site se génère correctement.
