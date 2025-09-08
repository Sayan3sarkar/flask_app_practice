from os import getenv
from platform import node
from functools import cache
from app.util import get_app_version


@cache
def _get_app_hostname() -> str:
    return node()


class APIConfig:
    API_TITLE = "Classroom"
    OPENAPI_VERSION = "3.1.0"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.28.1/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_UI_URL = (
        "https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"
    )

    API_VERSION = "v1"
    VERSION = get_app_version()
    DEBUG = getenv("DEBUG", "False").lower() == "true"
    APP_HOST = getenv("APP_HOST", "0.0.0.0")
    APP_PORT = int(getenv("APP_PORT", "5000"))
    HOSTNAME = _get_app_hostname()
