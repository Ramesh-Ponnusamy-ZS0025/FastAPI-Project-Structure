# src/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"  # default for dev
    # You can add more configs here, like JWT_SECRET, AWS keys, etc.

    class Config:
        env_file = ".env"  # load from .env file

# Create a single instance that will be imported elsewhere
settings = Settings()
