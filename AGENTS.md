AGENTS.md – Guidelines pour l’Agent

Ce dépôt contient :

    Un backend FastAPI géré par Docker,

    Un client Godot.

L’agent doit appliquer rigoureusement les instructions suivantes. Ces directives sont alignées sur les meilleures pratiques du secteur et assurent un workflow fiable, lisible et maintenable.
1. Principes Généraux

    Effectue des commits brefs, explicites et rédigés à l’impératif, en anglais.

    Crée une branche distincte pour chaque nouvelle fonctionnalité ou correction de bug.

    Soumets toutes tes modifications via une pull request (PR) pour garantir une revue de code systématique.

    Couvre chaque nouvelle fonctionnalité avec des tests automatiques.

    Documente tout code et tout comportement non trivial.

    Applique un formatage uniforme (utilise black pour le Python).

    Maintiens un environnement reproductible grâce à Docker.

    Vérifie régulièrement la sécurité et mets à jour les dépendances.

    Automatise les tâches répétitives (lint, tests) via l’intégration continue (CI).

2. Tests & Qualité du Code

    Teste systématiquement tout fichier Python modifié dans backend/app avec :

    pytest -q

    Ajoute des tests pour toute nouvelle fonctionnalité dans backend/tests.

3. Style et Formatage

    Formate tout code Python avec :

    black backend/app

    Vérifie que le style reste cohérent sur tout le projet.

4. Gestion des Commits & Branches

    Rédige des messages de commit concis, à l’impératif, en anglais (ex. : Add authentication middleware).

    Utilise une branche dédiée pour chaque évolution ou correctif.

5. Pull Requests (PR)

    Soumets chaque modification via une PR pour validation.

    Commence le titre de ta PR par l’emoji 🤖.

    Assure-toi que la PR décrit clairement la modification proposée.

6. Documentation & Automatisation

    Documente tout changement ou nouvelle fonctionnalité.

    Automatise le linting, les tests et la CI.

    Maintiens un environnement de développement reproductible avec Docker.

    Surveille les dépendances et mets-les à jour régulièrement.

7. Documentation Technique

    Vérifie que la documentation dans docs/ et la configuration mkdocs.yml sont à jour.

    Ajoute tout nouvel article Markdown au sommaire de mkdocs.yml et lie la page depuis docs/index.md.

    Décris la pile technique et explique le code en profondeur.

    Valide la génération du site documentaire avec :

    mkdocs build

8. Méthode Diátaxis

Respecte la structure **Diátaxis** pour toute la documentation :

    - **Tutoriels** : guides pas à pas pour débutants.
    - **Guides pratiques** : réponses rapides à un besoin précis.
    - **Référence** : description factuelle et exhaustive de l’API ou des fichiers.
    - **Explications** : contexte et choix techniques détaillés.

Classe chaque nouvelle page dans la bonne catégorie et maintiens un sommaire clair.

9. Règle d’Or

Toutes ces consignes s’appliquent à l’ensemble du dépôt, sans exception.

Fin du fichier.