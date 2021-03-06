from pydantic import BaseSettings
import pathlib
import os


class Settings(BaseSettings):
    DEBUG: bool = False
    DATABASE_HOST: str
    DATABASE_PORT: str = '3306'
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    OUTPUT_PATH: str = pathlib.Path(__file__).parent.resolve()
    PROCESS_WORKER_NUM: int = os.cpu_count()

    class Config:
        env_file = ".env"
