from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv

# Ensure environment variables from the project's .env file are loaded so that
# modules using `os.getenv` have access to them as well.
load_dotenv(find_dotenv())


class Settings(BaseSettings):
    ollama_text_model: str = "llama2"
    STABLEDIFFUSION_MODEL: str = "llava:7b"
    ollama_text_host: str = "ollama"
    ollama_text_port: int = 11434
    STABLEDIFFUSION_HOST: str = "stablediffusion"
    STABLEDIFFUSION_PORT: int = 7860

    class Config:
        env_prefix = ""
        env_file = find_dotenv()
        case_sensitive = False


settings = Settings()
