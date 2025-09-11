# Register blueprints for students
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, Response
from app.services import StudentService
from app.util import validate_schema
from app.dtos import CreateStudentDto, UpdateStudentDto

student_api = Blueprint("student", __name__)


class Student(MethodView):
    def get(self, student_id: int | None = None):
        if student_id is None:
            return self.get_all()
        """
        Fetch single student details
        """
        return StudentService().fetch_single_student(student_id), 200

    def get_all(self):
        """
        Return list of all students
        """
        return StudentService().fetch_all_students(), 200

    @validate_schema(CreateStudentDto)
    def post(self, data: CreateStudentDto):
        """
        Create new student

        Args:
            data (CreateStudentDto): Student Creation Request Body
        """
        new_student = StudentService().create_student(data)
        return jsonify(new_student), 201

    @validate_schema(UpdateStudentDto)
    def patch(self, data: UpdateStudentDto, student_id: int):
        """
        Update existing student by id

        Args:
            data (UpdateStudentDto): Student details updation request body
            student_id (str): id of the student in database
        """

        return jsonify(StudentService().update_student(data, student_id)), 200

    def delete(self, student_id: int):
        """
        Delete existing student by id

        Args:
            student_id (str): id of student in database
        """
        StudentService().delete_student(student_id)
        return Response(status=204)


student_view = Student.as_view("student")

student_api.add_url_rule(
    "/students", view_func=student_view, methods=["GET"], defaults={"student_id": None}
)  # Get all students

student_api.add_url_rule(
    "/students", view_func=student_view, methods=["POST"]
)  # Create new User

student_api.add_url_rule(
    "/students/<int:student_id>",
    view_func=student_view,
    methods=["GET", "PATCH", "DELETE"],
)  # Fetch single user, update single user, delete single user
