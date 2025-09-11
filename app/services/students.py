from app.models.students import Student
from app.dtos import CreateStudentDto, UpdateStudentDto
from app.config import db
from werkzeug.exceptions import BadRequest, NotFound
from sqlalchemy.orm import subqueryload


class StudentService:
    def fetch_all_students(self) -> list[dict]:
        students: list[Student] = Student.query.options(
            subqueryload(
                # Used to prevent N + 1 queries while trying to access Student.courses
                Student.courses
            )
        ).all()
        return [
            {
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "courses": [course.to_dict() for course in student.courses],
            }
            for student in students
        ]

    def create_student(self, createStudentDto: CreateStudentDto):
        existing_student = Student.query.filter_by(email=createStudentDto.email).first()
        if existing_student:
            raise BadRequest(
                description=f"User with email: {existing_student.email} already exists"
            )

        new_student = Student(**createStudentDto.model_dump())
        try:
            db.session.add(new_student)
            db.session.commit()
            return new_student.to_dict()
        except Exception as e:
            db.session.rollback()
            raise e

    def fetch_single_student(self, student_id: int) -> dict:
        student: Student | None = (
            Student.query.options(
                subqueryload(  # Used to prevent N + 1 queries while trying to access Student.courses
                    Student.courses
                )
            )
            .filter_by(id=student_id)
            .first()
        )

        if student is None:
            raise NotFound(description=f"No student having id: {student_id} exists")

        return {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "courses": [course.to_dict() for course in student.courses],
        }

    def update_student(
        self, updateStudentDto: UpdateStudentDto, student_id: int
    ) -> dict[str, str | int]:
        student = db.get_or_404(
            Student,
            student_id,
            description=f"No student having id: {student_id} exists",
        )
        update_data = updateStudentDto.model_dump(exclude_unset=True)

        try:
            for key, value in update_data.items():
                setattr(student, key, value)
            db.session.commit()
            return student.to_dict()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_student(self, student_id: int) -> None:
        student = db.get_or_404(
            Student,
            student_id,
            description=f"No student having id: {student_id} exists",
        )
        try:
            db.session.delete(student)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
