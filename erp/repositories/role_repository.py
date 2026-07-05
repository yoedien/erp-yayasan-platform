from sqlalchemy import select

from erp.models import Role
from .base_repository import BaseRepository


class RoleRepository(BaseRepository):

    def get_all(self):
        return self.session.scalars(
            select(Role).order_by(Role.id)
        ).all()

    def get_by_name(self, name: str):
        return self.session.scalar(
            select(Role).where(Role.name == name)
        )

    def create(self, name: str):
        role = Role(name=name)

        self.session.add(role)
        self.session.commit()
        self.session.refresh(role)

        return role