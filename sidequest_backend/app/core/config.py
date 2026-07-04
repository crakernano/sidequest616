import os
from pathlib import Path

try:
    import pydantic
    pydantic_version = tuple(int(x) for x in pydantic.VERSION.split(".") if x.isdigit())
except Exception:
    pydantic_version = (0, 0)

class settings:
    JWT_SECRET:str = os.getenv("SECRET_KEY","mysecretkey")
    JWT_ALGORITHM: str = os.getenv("ALGORITHM","HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES:int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


def _load_dotenv_if_present():
    # lazy import to avoid adding dependency if not needed
    try:
        from dotenv import load_dotenv

        env_path = Path(__file__).resolve().parents[2] / "siderequest_backend" / ".env"
        if not env_path.exists():
            env_path = Path(__file__).resolve().parents[2] / ".env"
        if env_path.exists():
            load_dotenv(env_path)
    except Exception:
        # no dotenv available or .env missing: skip
        pass


if pydantic_version[0] >= 2:
    # prefer to use pydantic-settings if available
    try:
        from pydantic_settings import BaseSettings  # type: ignore

        class Settings(BaseSettings):
            project_name: str = "Plans API"
            database_url: str = "postgresql://user:password@localhost:5432/plans_db"

            model_config = {"env_file": ".env"}

        settings = Settings()
    except Exception:
        # pydantic v2 installed but pydantic-settings not available; fallback to env read
        _load_dotenv_if_present()

        class Settings:
            project_name: str
            database_url: str

            def __init__(self):
                self.project_name = os.getenv("PROJECT_NAME", "Plans API")
                self.database_url = os.getenv(
                    "DATABASE_URL", "postgresql://user:password@localhost:5432/plans_db"
                )

        settings = Settings()
else:
    # pydantic v1 or not installed
    try:
        from pydantic import BaseSettings  # type: ignore

        class Settings(BaseSettings):
            project_name: str = "Plans API"
            database_url: str = "postgresql://user:password@localhost:5432/plans_db"

            class Config:
                env_file = ".env"


        settings = Settings()
    except Exception:
        # pydantic not available; fallback to simple env-based settings
        _load_dotenv_if_present()

        class Settings:
            project_name: str
            database_url: str

            def __init__(self):
                self.project_name = os.getenv("PROJECT_NAME", "Plans API")
                self.database_url = os.getenv(
                    "DATABASE_URL", "postgresql://user:password@localhost:5432/plans_db"
                )

        settings = Settings()
