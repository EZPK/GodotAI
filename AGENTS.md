# AGENTS.md – Directives pour l’Agent Codex

Ce dépôt contient :

- Un backend FastAPI géré par Docker
- Un client Godot

L’agent Codex doit suivre rigoureusement les instructions ci-dessous, alignées sur les meilleures pratiques du secteur, pour assurer un workflow fiable, lisible et maintenable.

## 1. Principes Généraux

- Effectuer des commits brefs, explicites et rédigés à l’impératif, en anglais.
- Créer une branche distincte pour chaque nouvelle fonctionnalité ou correction de bug.
- Soumettre toutes les modifications via une pull request (PR) pour garantir une revue de code systématique.
- Couvrir chaque nouvelle fonctionnalité avec des tests automatiques.
- Documenter tout code et comportement non trivial.
- Mettre en avant les informations importantes avec des warnings, tips, hints, etc.
- Appliquer un formatage uniforme (utiliser black pour le Python).
- Maintenir un environnement reproductible grâce à Docker.
- Vérifier régulièrement la sécurité et mettre à jour les dépendances.
- Automatiser les tâches répétitives (lint, tests) via l’intégration continue (CI).

## 2. Workflow Git Flow

Le projet suit le modèle Git Flow, structuré comme suit :

- main : branche de production contenant le code stable.
- develop : branche d'intégration pour les fonctionnalités en cours de développement.
- feature/* : branches pour le développement de nouvelles fonctionnalités, créées à partir de develop.
- release/* : branches pour préparer les nouvelles versions, créées à partir de develop.
- hotfix/* : branches pour corriger rapidement des bugs en production, créées à partir de main.

L'agent Codex doit :

- Créer des branches feature/* pour chaque nouvelle fonctionnalité.
- Créer des branches release/* pour préparer les versions stables.
- Créer des branches hotfix/* pour les corrections urgentes en production.
- Fusionner les branches feature/* dans develop via des PRs.
- Fusionner les branches release/* dans main et develop via des PRs.
- Fusionner les branches hotfix/* dans main et develop via des PRs.

## 3. Tests & Qualité du Code

- Tester systématiquement tout fichier Python modifié dans backend/app avec :

  - pytest -q

- Ajouter des tests pour toute nouvelle fonctionnalité dans backend/tests.

## 4. Style et Formatage

- Formater tout code Python avec :

  - black backend/app

- Vérifier que le style reste cohérent sur tout le projet.

## 5. Gestion des Commits & Branches

- Rédiger des messages de commit concis, à l’impératif, en anglais (ex. : Add authentication middleware).
- Utiliser une branche dédiée pour chaque évolution ou correctif.
- Respecter la structure des branches selon Git Flow.

## 6. Pull Requests (PR)

- Soumettre chaque modification via une PR pour validation.
- Commencer le titre de la PR par l’emoji 🤖.
- Assurer que la PR décrit clairement la modification proposée.

## 7. Documentation & Automatisation

- Documenter tout changement ou nouvelle fonctionnalité.
- Automatiser le linting, les tests et la CI.
- Maintenir un environnement de développement reproductible avec Docker.
- Surveiller les dépendances et les mettre à jour régulièrement.
- Garantir un ton aimable et sympathique dans la rédaction de la documetation avec:

    - vale docs/

## 8. Documentation Technique

- Vérifier que la documentation dans docs/ et la configuration mkdocs.yml sont à jour.
- Ajouter tout nouvel article Markdown au sommaire de mkdocs.yml et lier la page depuis docs/index.md.
- S'assurer que les fichiers renseignés dans des index.md sont toujours mis en forme sous forme de liens.
- Décrire la pile technique et expliquer le code en profondeur.
- Ajouter une section FAQ uniquement lorsque c'est pertinent. Elle doit contenir des questions réellement intéressantes pour les lecteurs, sans texte de remplissage ni questions évidentes.
- Valider la génération du site documentaire avec :

  - mkdocs build

- Garantir la qualité ainsi qu'uun ton aimable et sympathique dans la rédaction de la documentation avec:

  - vale docs/

## 9. Méthode Diátaxis

Respecter la structure Diátaxis pour toute la documentation :

- Tutoriels : guides pas à pas pour débutants.
- Guides pratiques : réponses rapides à un besoin précis.
- Référence : description factuelle et exhaustive de l’API ou des fichiers.
- Explications : contexte et choix techniques détaillés.

Classer chaque nouvelle page dans la bonne catégorie et maintenir un sommaire clair.

## 10. Règle d’Or

Toutes ces consignes s’appliquent à l’ensemble du dépôt, sans exception.
