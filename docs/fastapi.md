# ⚡ FastAPI

FastAPI est un framework Web moderne et asynchrone pour Python.
Dans **GodotAI**, il expose les routes HTTP utilisées par le client Godot et gère la base SQLite.

## Exemple minimal
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
```

- [Documentation officielle](https://fastapi.tiangolo.com/)
