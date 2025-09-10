# Register blueprints for students
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify, Response

student_api = Blueprint("student", __name__)


class Student(MethodView):
    def get(self, student_id=None):  # Get singular student details by student_id
        if student_id is None:
            return self.get_all()
        return jsonify({}), 200

    def get_all(self):  # Return list of all students
        return [], 200

    def post(self):  # Create new student
        return jsonify({}), 201

    def put(self, student_id: str):  # Update existing student by id
        return jsonify({}), 200

    def delete(self, student_id: str):  # Delete existing student by id
        return Response(status=204)


student_view = Student.as_view("student")

student_api.add_url_rule(
    "/students", view_func=student_view, methods=["GET"], defaults={"student_id": None}
)  # Get all students

student_api.add_url_rule(
    "/students", view_func=student_view, methods=["POST"], defaults={"student_id": None}
)  # Create new User

student_api.add_url_rule(
    "/students/<int:student_id>",
    view_func=student_view,
    methods=["GET", "PUT", "DELETE"],
)  # Fetch single user, update single user, delete single user
