from datetime import datetime, timezone
from sqlalchemy.orm import declarative_mixin, mapped_column, Mapped
from sqlalchemy import TIMESTAMP
from typing import Optional


@declarative_mixin
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
