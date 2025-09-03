import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")
    LLM_API_URL: str = os.getenv("LLM_API_URL", "https://api.openai.com/v1/completions")
    LLM_MODEL_NAME: str = os.getenv("LLM_MODEL_NAME", "gpt-3.5-turbo")
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    LLM_MAX_TOKENS: int = int(os.getenv("LLM_MAX_TOKENS", "1000"))
    
    PDF_MAX_FILE_SIZE_MB: int = int(os.getenv("PDF_MAX_FILE_SIZE_MB", "10"))
    PDF_ALLOWED_MIME_TYPES: list = ["application/pdf"]
    
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()