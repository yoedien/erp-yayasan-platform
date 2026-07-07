from sqlalchemy import select

from erp.models.permission import Permission
from .base_repository import BaseRepository


class PermissionRepository(BaseRepository):

    def get_all(self):

        return self.session.scalars(
            select(Permission).order_by(
                Permission.module,
                Permission.code,
            )
        ).all()

    def get_by_id(
        self,
        permission_id: int,
    ):

        return self.session.scalar(
            select(Permission).where(
                Permission.id == permission_id
            )
        )

    def get_by_code(
        self,
        code: str,
    ):

        return self.session.scalar(
            select(Permission).where(
                Permission.code == code
            )
        )

    def create(
        self,
        code: str,
        name: str,
        module: str,
        description: str | None = None,
    ):

        permission = Permission(
            code=code,
            name=name,
            module=module,
            description=description,
        )

        self.session.add(permission)

        self.session.commit()

        self.session.refresh(permission)

        return permission

    def update(
        self,
        permission,
        code: str,
        name: str,
        module: str,
        description: str | None = None,
    ):

        permission.code = code
        permission.name = name
        permission.module = module
        permission.description = description

        self.session.commit()

        self.session.refresh(permission)

        return permission

    def delete(
        self,
        permission,
    ):

        self.session.delete(permission)

        self.session.commit()