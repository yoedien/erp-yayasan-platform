from sqlalchemy import select

from erp.models import RolePermission


class RolePermissionRepository:

    def __init__(self, session):
        self.session = session

    def get_by_role(self, role_id: int):

        return self.session.scalars(
            select(RolePermission).where(
                RolePermission.role_id == role_id
            )
        ).all()

    def get(
        self,
        role_id: int,
        permission_id: int,
    ):

        return self.session.scalar(
            select(RolePermission).where(
                RolePermission.role_id == role_id,
                RolePermission.permission_id == permission_id,
            )
        )

    def create(
        self,
        role_id: int,
        permission_id: int,
    ):

        item = RolePermission(
            role_id=role_id,
            permission_id=permission_id,
        )

        self.session.add(item)

        self.session.commit()

        self.session.refresh(item)

        return item

    def delete(
        self,
        item,
    ):

        self.session.delete(item)

        self.session.commit()