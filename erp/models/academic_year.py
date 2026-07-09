from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from erp.database.base import Base
from sqlalchemy.orm import relationship

class AcademicYear(Base):
    __tablename__ = "academic_years"

    id: Mapped[int] = mapped_column(primary_key=True)

    code: Mapped[str] = mapped_column(
        String(10),
        unique=True,
    )

    name: Mapped[str] = mapped_column(
        String(30),
    )

    start_date: Mapped[datetime] = mapped_column(
        Date,
    )

    end_date: Mapped[datetime] = mapped_column(
        Date,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    fund_sources = relationship(
        "FundSource",
        back_populates="academic_year",
        cascade="all, delete-orphan",
    )
