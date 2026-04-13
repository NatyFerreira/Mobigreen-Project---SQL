from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr
import os


class Settings(BaseSettings):
    DB_USER: SecretStr | None = None
    DB_PASSWORD: SecretStr | None = None
    DB_HOST: str | None = None
    DB_PORT: int | None = None
    DB_NAME: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"   # <— IGNORA VARIÁVEIS EXTRAS DO .env

    def _fallback(self, primary: str | None, fallback_env: str) -> str:
        if primary not in (None, "", "None"):
            return primary
        return os.getenv(fallback_env)

    @property
    def DATABASE_URL(self) -> str:
        user = self._fallback(
            self.DB_USER.get_secret_value() if self.DB_USER else None,
            "POSTGRES_USER"
        )
        password = self._fallback(
            self.DB_PASSWORD.get_secret_value() if self.DB_PASSWORD else None,
            "POSTGRES_PASSWORD"
        )
        host = self._fallback(self.DB_HOST, "POSTGRES_HOST")
        port = self._fallback(str(self.DB_PORT) if self.DB_PORT else None, "POSTGRES_PORT")
        name = self._fallback(self.DB_NAME, "POSTGRES_DB")

        return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


settings = Settings()
