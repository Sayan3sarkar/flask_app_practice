from typing import TYPE_CHECKING, Union
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.config.database_config import db

from app.models import TimestampMixin
from app.models.course_registration import course_registration

# Type checker perceives this as true, but at run time it's false - so no circular import
# Done to avoid type checker errors
if TYPE_CHECKING:
    from app.models.courses import Course


class Student(db.Model, TimestampMixin):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    courses: Mapped[list["Course"]] = relationship(
        secondary=course_registration, back_populates="students"
    )

    def __repr__(self) -> str:
        super()
        return f"Student {self.name} having email: {self.created_at}"

    def to_dict(self) -> dict[str, Union[str, int]]:
        return {"id": self.id, "name": self.name, "email": self.email}
