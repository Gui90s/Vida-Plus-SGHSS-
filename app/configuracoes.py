from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "minha_chave_secreta_super_segura"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
