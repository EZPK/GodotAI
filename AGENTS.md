# AGENTS.md - Directives pour l'agent

Ce dépôt rassemble un backend **FastAPI** piloté par Docker ainsi qu'un client **Godot**. L'agent qui contribue ici doit respecter les instructions suivantes, inspirées des bonnes pratiques de l'industrie :

## Principes clés

- Adopter des commits courts au message clair et rédigé à l'impératif.
- Créer une branche dédiée pour chaque fonctionnalité ou correctif.
- Soumettre toute modification via une pull request pour faciliter la revue de code.
- Couvrir les nouvelles fonctionnalités par des tests automatiques.
- Documenter le code et les comportements attendus.
- Appliquer un formatage cohérent, par exemple `black` pour Python.
- Maintenir un environnement reproductible grâce aux conteneurs Docker.
- Vérifier régulièrement la sécurité et mettre à jour les dépendances.
- Automatiser les tâches répétitives (lint, tests) via l'intégration continue.

1. **Tester le code Python**
   - Si une modification touche des fichiers Python (dossier `backend/app`), exécuter `pytest -q` pour vérifier que tout passe, même s'il n'y a pas encore de tests.
   - Ajouter des tests dans `backend/tests` pour toute nouvelle fonctionnalité.

2. **Style de code et formatage**
   - Utiliser `black` pour formater le Python.
   - Exemple de commande :
     ```bash
     black backend/app
     ```

3. **Commits et branches**
   - Rédiger des messages de commit concis à l'impératif en anglais, par ex. `Add example API endpoint`.
   - Créer une branche dédiée pour chaque fonctionnalité ou correctif.

4. **Pull requests**
   - Soumettre toute modification via une pull request pour faciliter la revue de code.
   - Le message de la pull request doit commencer par l'emoji `🤖`.

5. **Documentation et automatisation**
   - Documenter le code et les comportements attendus.
   - Automatiser les tâches répétitives (lint, tests) via l'intégration continue.
   - Maintenir un environnement reproductible grâce à Docker.
   - Vérifier régulièrement la sécurité et mettre à jour les dépendances.

Ces consignes s'appliquent à l'ensemble du dépôt.

6. **Documentation**
   - Vérifier que la documentation dans `docs/` et `mkdocs.yml` reste fidèle au fonctionnement actuel du projet.
   - Ajouter tout nouvel article Markdown au sommaire de `mkdocs.yml` et lier la page depuis `docs/index.md`.
   - Les pages doivent détailler la pile technique et expliquer le code de ce dépôt en profondeur.
   - Après chaque mise à jour de la documentation, exécuter `mkdocs build` pour s'assurer que le site se génère correctement.
