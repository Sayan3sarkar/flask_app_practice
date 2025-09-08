from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from app.models import TimestampMixin
from app.config.database_config import db


class Student(db.Model, TimestampMixin):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        super()
        return f"Student {self.name} having email: {self.created_at}"
