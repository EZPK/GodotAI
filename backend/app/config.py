from pydantic import BaseSettings


class Settings(BaseSettings):
    ollama_text_model: str = "llama2"
    STABLEDIFFUSION_MODEL: str = "llava:7b"
    ollama_text_host: str = "ollama"
    ollama_text_port: int = 11434
    STABLEDIFFUSION_HOST: str = "stablediffusion"
    STABLEDIFFUSION_PORT: int = 7860

    class Config:
        env_prefix = ""
        env_file = ".env"
        case_sensitive = False


settings = Settings()
