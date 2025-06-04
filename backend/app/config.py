from pydantic import BaseSettings


class Settings(BaseSettings):
    ollama_text_model: str = "llama2"
    ollama_image_model: str = "llava:7b"
    ollama_text_host: str = "ollama"
    ollama_text_port: int = 11434
    ollama_image_host: str = "stablediffusion"
    ollama_image_port: int = 7860

    class Config:
        env_prefix = ""
        env_file = ".env"
        case_sensitive = False


settings = Settings()
