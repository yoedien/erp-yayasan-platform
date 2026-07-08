from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models import (
    RolePermission,
)


class PermissionChecker:

    @staticmethod
    def has_permission(
        role_id: int,
        permission_code: str,
    ) -> bool:

        session = SessionLocal()

        try:

            permission = session.scalar(
                select(RolePermission)
                .join(RolePermission.permission)
                .where(
                    RolePermission.role_id == role_id,
                    RolePermission.permission.has(
                        code=permission_code
                    ),
                )
            )

            return permission is not None

        finally:

            session.close()