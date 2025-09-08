from sqlalchemy import Text, String, Date
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional
from datetime import date

from app.models import TimestampMixin
from app.config.database_config import db


class Course(db.Model, TimestampMixin):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
