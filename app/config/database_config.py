from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from typing import Union

from app.models import Base
from app.util import get_required_env


class DatabaseConfig:
    SQLALCHEMY_DATABASE_ENDPOINT = get_required_env("SQLALCHEMY_DATABASE_ENDPOINT")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{SQLALCHEMY_DATABASE_ENDPOINT}"
    SQLALCHEMY_ENGINE_OPTIONS: dict[str, Union[int, str]] = {
        "max_overflow": 10,
        "pool_pre_ping": True,
        "isolation_level": "READ COMMITTED",
        "pool_recycle": 1800,
        "pool_size": 5,
        "pool_use_lifo": True,
        "pool_timeout": 15,
    }


db = SQLAlchemy(model_class=Base)
migrate = Migrate(db=db)
