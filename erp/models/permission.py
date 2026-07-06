from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from erp.database.base import Base


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)

    code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    module: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    role_permissions = relationship(
    "RolePermission",
    back_populates="permission",
    cascade="all, delete-orphan",
)