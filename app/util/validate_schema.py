from functools import wraps
from flask import request, jsonify
from pydantic import BaseModel, ValidationError


def validate_schema(schema: type[BaseModel]):
    """
    Decorator to validate incoming JSON against a Pydantic schema.
    - If validation succeeds: passes validated data to the view as `data`.
    - If validation fails: returns 400 with details.
    """

    def decorator(fn):
        @wraps(fn)  # preserves fn properties like __name__, __meta__ etc
        def wrapper(*args, **kwargs):
            try:
                # Parse and validate request JSON
                payload = request.get_json(force=True, silent=True)
                data = schema.model_validate(payload)
            except ValidationError as e:
                return jsonify({"errors": e.errors()}), 400

            return fn(*args, data=data, **kwargs)

        return wrapper

    return decorator
