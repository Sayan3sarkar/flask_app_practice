from flask import Flask
from flask_smorest import Api
from werkzeug.exceptions import HTTPException

from app.config import APIConfig, DatabaseConfig, db, migrate
from app.util import register_all_errors, handle_exception


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(APIConfig)
    app.config.from_object(DatabaseConfig)
    api = Api(app)
    db.init_app(app)  # Database initialization
    migrate.init_app(app)  # Migration initialization

    # Model imports necessary here to avoid circular imports and cross-references in mind
    from app.models.courses import Course
    from app.models.students import Student

    # Route imports
    from app.routes import health_api, student_api, course_api

    api.register_blueprint(health_api)
    api.register_blueprint(student_api)
    api.register_blueprint(course_api)

    # Global error handler
    register_all_errors(app, handle_exception)

    return app


def main():
    app = create_app()
    app.run(debug=APIConfig.DEBUG, port=APIConfig.APP_PORT, host=APIConfig.APP_HOST)


if __name__ == "main":
    main()
