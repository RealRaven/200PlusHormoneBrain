from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    model_id: str = "google/gemma-2-2b-it"
    vllm_base_url: str = "http://vllm:8001/v1"
    vllm_api_key: str = "EMPTY"

    gateway_host: str = "0.0.0.0"
    gateway_port: int = 8000

    max_tokens: int = 512
    temperature: float = 0.7

    data_dir: str = "data"
    memory_file: str = "data/memory.json"
    chemistry_dir: str = "infrastructure/chemicals_hormones"


settings = Settings()