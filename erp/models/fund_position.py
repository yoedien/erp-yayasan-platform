from datetime import datetime

from sqlalchemy import (
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Numeric,
    Integer,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from erp.database.base import Base


class FundPosition(Base):

    __tablename__ = "fund_positions"

    id: Mapped[int] = mapped_column(primary_key=True)

    fund_source_id: Mapped[int] = mapped_column(ForeignKey("fund_sources.id"))

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
    )

    budget: Mapped[float] = mapped_column(
        Numeric(18, 2),
        default=0,
    )

    priority: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    budget_locked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )

    fund_source = relationship(
        "FundSource",
        back_populates="fund_positions",
    )
