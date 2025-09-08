from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """_description_

    Instead of using `declarative_base`, we go ahead and use the `DeclarativeBase` for a class based instantiation,
    the only reason for this was to set the naming conventions
    """

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(table_name)s_%(column_0_N_name)s",
            "uq": "uq_%(table_name)s_%(column_0_N_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_N_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
