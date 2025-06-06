import os
from importlib import reload

import backend.app.config as config


def test_env_loaded():
    reload(config)  # ensure dotenv is loaded
    assert config.settings.ollama_text_model == "smollm:latest"
    assert os.getenv("OLLAMA_TEXT_MODEL") == "smollm:latest"
