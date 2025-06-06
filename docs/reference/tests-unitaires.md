# ✅ Tests unitaires

Cette page explique comment lancer les tests unitaires du backend.

Les tests sont écrits avec **pytest** et se trouvent dans le dossier `backend/tests/`.
Pour exécuter l'ensemble des tests :

```bash
pytest -q
```

Exemple de test issu du fichier `test_root.py` :

```python
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["message"] == "Backend FastAPI fonctionne !"
```

Pour cibler un seul test pendant le développement :

```bash
pytest backend/tests/test_root.py::test_read_root -q
```

Les dépendances nécessaires sont listées dans `backend/requirements.txt`.
Avant de lancer les tests pour la première fois, installez-les avec :

```bash
make install
```

Chaque nouvelle fonctionnalité Python doit être accompagnée d'un test
correspondant dans ce répertoire.

## Voir aussi

- [Tests E2E](tests-e2e.md)
- [AGENTS.md](agents-file.md)
