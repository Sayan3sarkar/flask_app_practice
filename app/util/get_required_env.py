from os import getenv


def get_required_env(key: str) -> str:
    value = getenv(key)
    if not value:
        raise ValueError(f"{key} is required")
    return value
