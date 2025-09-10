from flask import Flask
from flask_smorest import Api

from app.config import APIConfig, DatabaseConfig, db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(APIConfig)
    app.config.from_object(DatabaseConfig)
    api = Api(app)
    db.init_app(app)  # Database initialization
    migrate.init_app(app)  # Migration initialization

    from app.routes import health_api, student_api, course_api

    api.register_blueprint(health_api)
    api.register_blueprint(student_api)
    api.register_blueprint(course_api)

    return app


def main():
    app = create_app()
    app.run(debug=APIConfig.DEBUG, port=APIConfig.APP_PORT, host=APIConfig.APP_HOST)


if __name__ == "main":
    main()
