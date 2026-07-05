from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from erp.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id")
    )

    unit_id: Mapped[int] = mapped_column(
        ForeignKey("units.id")
    )

    role = relationship("Role", back_populates="users")
    unit = relationship("Unit", back_populates="users")