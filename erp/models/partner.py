from sqlalchemy import (
    Boolean,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from erp.database.base import Base


class Partner(Base):

    __tablename__ = "partners"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
    )

    partner_type: Mapped[str] = mapped_column(
        String(30),
    )

    pic: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    phone: Mapped[str] = mapped_column(
        String(30),
        default="",
    )

    email: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    address: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    city: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    npwp: Mapped[str] = mapped_column(
        String(50),
        default="",
    )

    notes: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    def __repr__(self):
        return (
            f"<Partner("
            f"{self.code}, "
            f"{self.name})>"
        )