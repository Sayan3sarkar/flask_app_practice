from app.models.base import Base
from app.models.timestamp_mixin import TimestampMixin

# NOTE: DO NOT add Concrete models here - prevents circular dependency on db imports
__all__ = ["Base", "TimestampMixin"]
