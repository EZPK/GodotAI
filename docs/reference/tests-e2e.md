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

Extrait du fichier `test_api_playwright.py` :

```python
from playwright.sync_api import sync_playwright

def test_root_endpoint():
    with sync_playwright() as p:
        request = p.request.new_context(base_url="http://127.0.0.1:8002")
        resp = request.get("/")
        assert resp.status == 200
```

## Voir aussi

- [Tests unitaires](tests-unitaires.md)
- [Guide de démarrage](../tutoriels/premiers-pas.md)
