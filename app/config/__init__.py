from dotenv import load_dotenv
from os.path import join, dirname

from app.config.api_config import APIConfig
from app.config.database_config import DatabaseConfig, db, migrate

load_dotenv(join(dirname(__file__), "..", "..", ".env"))

__all__ = ["APIConfig", "DatabaseConfig", "db", "migrate"]
