from flask import jsonify
from flask_smorest import Blueprint
from flask.views import MethodView

from app.services import HealthCheckService

health_api = Blueprint("health_check", __name__)


# @health_api.route("/health") # this only works since we are using flask-smorest's Blueprint class, using flask's native Blueprint with this approach won't work
class HealthCheck(MethodView):
    def get(self):
        body = HealthCheckService().check()
        status_code = 200 if body.get("healthy", True) else 500
        return jsonify(body), status_code


# Comment the following 2 lines when NOT using @flask-smorest's Blueprint.route on the class
health_view = HealthCheck.as_view("health_view")
health_api.add_url_rule("/health", view_func=health_view)
