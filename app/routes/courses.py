# Register Blueprints for Courses
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request, jsonify, Response


def str_to_int_list(comma_separated_string: str) -> list[int]:
    """
    Summary:
    Takes in a comma_separated_string having integer values(usually query params - integer values) and return a list of integers

    Args:
        comma_separated_string (str): "1,2,3"

    Returns:
        list[int]: [1,2,3]
    """
    try:
        return list(map(int, comma_separated_string.split(",")))
    except Exception as e:
        raise ValueError(
            f"Some error encountered while converting query params to list: {e}"
        )


course_api = Blueprint("course", __name__)


class Course(MethodView):
    def get(self, course_id=None):
        if course_id is None:
            return self.get_all()
        return jsonify({}), 200

    def get_all(self):  # Return list of all courses
        return [], 200

    def post(self):  # Create new course
        return jsonify({}), 201

    def put(self, course_id: str):  # Update existing course by id
        return jsonify({}), 200

    def delete(self, course_id: str):  # Delete existing course by id
        return Response(status=204)

    def add_students_to_course(self, course_id: str):
        try:
            student_ids = str_to_int_list(request.args.get("student_ids", ""))
            return jsonify({"course_id": course_id, "student_ids": student_ids}), 200
        except Exception:
            return jsonify({"error": "Invalid Query Params"}), 400

    def remove_student_from_course(self, course_id: str):
        try:
            student_ids = str_to_int_list(request.args.get("student_ids", ""))
            return jsonify({"course_id": course_id, "student_ids": student_ids}), 200
        except Exception:
            return jsonify({"error": "Invalid Query Params"}), 400


course_view = Course.as_view("student")
course_api.add_url_rule(
    "/courses", view_func=course_view, methods=["GET"], defaults={"course_id": None}
)  # Get all students
course_api.add_url_rule(
    "/courses", view_func=course_view, methods=["POST"], defaults={"course_id": None}
)
course_api.add_url_rule(
    # accept query params `?student_ids=[1,2,3]`
    "/courses/<string:course_id>/assign",
    view_func=lambda course_id: Course().add_students_to_course(course_id),
    methods=["POST"],
)
course_api.add_url_rule(
    # accept query params `?student_ids=[1,2,3]`
    "/courses/<int:course_id>/unassign",
    view_func=lambda course_id: Course().remove_student_from_course(course_id),
    methods=["DELETE"],
)
course_api.add_url_rule(
    "/courses/<int:course_id>", view_func=course_view, methods=["GET", "PUT", "DELETE"]
)
