from datetime import datetime

from sqlalchemy import (
    String,
    Boolean,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from erp.database.base import Base


class FundSource(Base):

    __tablename__ = "fund_sources"

    id: Mapped[int] = mapped_column(primary_key=True)

    academic_year_id: Mapped[int] = mapped_column(ForeignKey("academic_years.id"))

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
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

    academic_year = relationship(
        "AcademicYear",
        back_populates="fund_sources",
    )

    fund_positions = relationship(
        "FundPosition",
        back_populates="fund_source",
        cascade="all, delete-orphan",
    )
