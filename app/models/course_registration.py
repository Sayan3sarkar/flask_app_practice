from sqlalchemy import Column, Integer, ForeignKey
from app.config import db

course_registration = db.Table(
    "course_registration",
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id")),
)
