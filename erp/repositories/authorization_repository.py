from sqlalchemy import select

from erp.models import (
    Permission,
    RolePermission,
    User,
)


class AuthorizationRepository:

    def __init__(self, session):

        self.session = session

    def get_permission_codes(
        self,
        user_id: int,
    ):

        stmt = (
            select(Permission.code)
            .join(
                RolePermission,
                Permission.id
                == RolePermission.permission_id,
            )
            .join(
                User,
                User.role_id
                == RolePermission.role_id,
            )
            .where(
                User.id == user_id
            )
        )

        return self.session.scalars(
            stmt
        ).all()