from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_PASS: str
    POSTGRES_USERNAME: str
    POSTGRES_ADDRESS: str
    POSTGRES_PORT: str
    POSTGRES_DBNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()