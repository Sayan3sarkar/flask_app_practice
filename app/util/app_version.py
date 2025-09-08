from functools import cache
from os.path import dirname, join


@cache
def get_app_version() -> str:
    with open(join(dirname(__file__), "..", "..", "VERSION"), "r") as f:
        return f.read().strip()


@cache
def get_version_or_unknown() -> str:
    try:
        return get_app_version()
    except FileNotFoundError:
        return "unknown"
