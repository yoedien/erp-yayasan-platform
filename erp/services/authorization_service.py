from sqlalchemy import select

from erp.models import (
    Permission,
    RolePermission,
)


class AuthorizationService:

    def __init__(self, session):
        self.session = session

    def has_permission(
        self,
        role_id: int,
        permission_code: str,
    ) -> bool:
        """
        Mengecek apakah suatu role memiliki permission tertentu.
        """

        stmt = (
            select(RolePermission)
            .join(Permission)
            .where(
                RolePermission.role_id == role_id,
                Permission.code == permission_code,
            )
        )

        return self.session.scalar(stmt) is not None

    def get_permissions(
        self,
        role_id: int,
    ) -> set[str]:
        """
        Mengambil seluruh permission milik suatu role.
        Hasil dikembalikan dalam bentuk set agar pencarian cepat.
        """

        stmt = (
            select(Permission.code)
            .join(RolePermission)
            .where(RolePermission.role_id == role_id)
        )

        return set(self.session.scalars(stmt).all())
