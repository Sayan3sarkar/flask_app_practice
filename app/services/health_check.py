from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any, cast
from sqlalchemy import text, QueuePool

from app.config import db, APIConfig
from app.util import get_version_or_unknown
from app.types import CheckToDictResponseType, HealthCheckResponseType


class Check(ABC):

    name: str
    _healthy: bool = False
    _msg: Any = None

    @abstractmethod
    def check(self) -> None:
        raise NotImplementedError

    def __bool__(self) -> bool:
        return self._healthy

    def to_dict(self) -> CheckToDictResponseType:
        return {"health": self._healthy, "msg": self._msg}


class PostgresCheck(Check):
    name = "Postgres"

    def check(self) -> None:
        try:
            with db.engine.connect() as conn:
                result = conn.execute(text("SELECT 1"))
                self._healthy = result.scalar() == 1
            pool = cast(QueuePool, db.engine.pool)
            self._msg = {
                "pool": {
                    "size": pool.size(),
                    "checkedIn": pool.checkedin(),
                    "checkedOut": pool.checkedout(),
                    "overflow": pool.overflow(),
                }
            }
        except Exception as e:
            pool = cast(QueuePool, db.engine.pool)
            self._msg = {
                "message": f"Postgres check failed: {str(e)}",
                "error": f"{type(e).__name__}: {str(e)}",
                "pool": {
                    "size": pool.size(),
                    "checkedIn": pool.checkedin(),
                    "checkedOut": pool.checkedout,
                    "overflow": pool.overflow(),
                },
            }


class HealthCheckService:

    def _checks(self) -> list[Check]:
        checks: list[Check] = [PostgresCheck()]
        for check in checks:
            check.check()
        return checks

    def check(self) -> HealthCheckResponseType:
        checks = self._checks()
        return {
            "created_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "hostname": APIConfig.HOSTNAME,
            "version": get_version_or_unknown(),
            "healthy": (
                all(checks) if checks else True
            ),  # checks base class __bool__, if not found reverts to __len__
            "checks": {check.name: check.to_dict() for check in checks},
        }
