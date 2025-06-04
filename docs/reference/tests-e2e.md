# 🚦 Tests E2E avec Playwright

Le projet propose également un exemple de test de bout en bout utilisant
**Playwright**. Ces tests vivent dans le dossier `e2e/`.

Pour installer Playwright et ses dépendances :

```bash
make install
# Optionnel : .venv/bin/playwright install
```

Lancez ensuite les tests E2E avec :

```bash
pytest e2e
```

Le script démarre brièvement le serveur FastAPI sur un port local puis effectue
un appel HTTP via l'API `request` de Playwright.
