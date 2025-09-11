from sqlalchemy import Text, String, Date
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional, TYPE_CHECKING
from datetime import date

from app.config.database_config import db

from app.models import TimestampMixin
from app.models.course_registration import course_registration

# Type checker perceives this as true, but at run time it's false - so no circular import
# Done to avoid type checker errors
if TYPE_CHECKING:
    from app.models.students import Student


class Course(db.Model, TimestampMixin):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    students: Mapped[list["Student"]] = relationship(
        secondary=course_registration, back_populates="courses"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
