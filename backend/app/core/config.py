# backend/app/core/config.py

import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

# Define the path to the .env file relative to this config file
# Goes up two levels from core/config.py to the backend/ directory
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    """

    # --- Project Settings ---
    PROJECT_NAME: str = "AI Performance Hub"
    API_V1_STR: str = "/api/v1"  # Base path for API v1 routes

    # --- Database Settings ---
    # Default to the SQLite database in the data directory
    # The format is important: sqlite+aiosqlite:///./path/to/db.file
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/aiphb.db"

    # --- Security Settings (JWT) ---
    # Generate a strong secret key using: openssl rand -hex 32
    # Store this securely, especially in production!
    SECRET_KEY: str = os.getenv("SECRET_KEY", "a_default_weak_secret_key_for_dev")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Default token expiry: 30 minutes

    # --- AI Service Settings ---
    # Placeholder for the API key of your chosen AI provider
    AI_API_KEY: str | None = os.getenv("AI_API_KEY", None)
    AI_MODEL_NAME: str = os.getenv(
        "AI_MODEL_NAME", "default-ai-model"
    )  # Example: Specify model if needed

    # --- CORS Settings (Cross-Origin Resource Sharing) ---
    # List of allowed origins for frontend access.
    # Use "*" for development only, be specific in production.
    # Example: ["http://localhost:5173", "https://your-frontend-domain.com"]
    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # Adjust as needed

    class Config:
        # Specifies the path to the .env file if you want pydantic-settings to load it
        # directly
        # Note: We are loading it manually above using python-dotenv for more control,
        # but keeping this structure is common practice.
        env_file = ".env"
        env_file_encoding = "utf-8"
        # Makes BaseSettings case-insensitive regarding environment variables
        case_sensitive = False


# Instantiate the settings object for easy import across the application
settings = Settings()

# Example usage (in other files):
# from app.core.config import settings
# db_url = settings.DATABASE_URL
# print(f"Connecting to database: {db_url}")
# print(f"Project Name: {settings.PROJECT_NAME}")
