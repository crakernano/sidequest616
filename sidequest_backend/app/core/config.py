from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Plans API"
    database_url: str = "postgresql://user:password@localhost:5432/plans_db"

    class Config:
        env_file = ".env"


settings = Settings()
