from sqlalchemy import select

from erp.models import Permission, RolePermission


class AuthorizationService:

    def __init__(self, session):
        self.session = session

    def has_permission(
        self,
        role_id: int,
        permission_code: str,
    ) -> bool:

        stmt = (
            select(RolePermission)
            .join(Permission)
            .where(
                RolePermission.role_id == role_id,
                Permission.code == permission_code,
            )
        )

        return self.session.scalar(stmt) is not None