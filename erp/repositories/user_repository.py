from sqlalchemy import select
from sqlalchemy.orm import joinedload

from erp.models import User
from .base_repository import BaseRepository


class UserRepository(BaseRepository):

    def get_all(self):
        return (
            self.session.scalars(
                select(User)
                .options(
                    joinedload(User.role),
                    joinedload(User.unit),
                )
                .order_by(User.id)
            )
            .unique()
            .all()
        )

    def get_by_id(self, user_id: int):
        return self.session.scalar(
            select(User).where(
                User.id == user_id
            )
        )

    def get_by_username(self, username: str):
        return self.session.scalar(
            select(User).where(
                User.username == username
            )
        )

    def create(
        self,
        username: str,
        password_hash: str,
        full_name: str,
        role_id: int,
        unit_id: int,
    ):

        user = User(
            username=username,
            password_hash=password_hash,
            full_name=full_name,
            role_id=role_id,
            unit_id=unit_id,
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def update(
        self,
        user,
        username: str,
        full_name: str,
        role_id: int,
        unit_id: int,
    ):

        user.username = username
        user.full_name = full_name
        user.role_id = role_id
        user.unit_id = unit_id

        self.session.commit()
        self.session.refresh(user)

        return user

    def update_password(
        self,
        user,
        password_hash: str,
    ):

        user.password_hash = password_hash

        self.session.commit()
        self.session.refresh(user)

        return user

    def delete(self, user):

        self.session.delete(user)

        self.session.commit()