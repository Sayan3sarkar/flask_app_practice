from typing import Callable
from flask import jsonify, Flask
from werkzeug.exceptions import HTTPException


def handle_exception(e):
    err = dict(
        code=getattr(e, "code", 500),
        message=getattr(e, "description", "Something went wrong"),
        error=getattr(e, "name", e.__class__.__name__),
    )
    return jsonify(err), err["code"]


def register_all_errors(app: Flask, error_handler: Callable):
    """
    Utility function to register all errors of the application in one place

    Args:
        app (Flask): The flask app instance
        error_handler (Callable): the error handler

    Examples:
        register_all_errors(app, error_handler)
    """
    exception_list = [HTTPException, Exception]

    for exception in exception_list:
        app.register_error_handler(exception, error_handler)
