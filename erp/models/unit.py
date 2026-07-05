from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from erp.database.base import Base


class Unit(Base):
    __tablename__ = "units"

    id: Mapped[int] = mapped_column(primary_key=True)

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    users = relationship("User", back_populates="unit")