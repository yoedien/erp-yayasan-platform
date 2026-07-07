from erp.database.session import SessionLocal
from erp.repositories.role_repository import RoleRepository


class RoleService:

    def get_roles(self):

        session = SessionLocal()

        try:
            repo = RoleRepository(session)
            return repo.get_all()

        finally:
            session.close()

    def create_role(
        self,
        name: str,
    ):

        session = SessionLocal()

        try:

            repo = RoleRepository(session)

            existing = repo.get_by_name(name)

            if existing:
                raise ValueError(
                    f"Role '{name}' sudah ada."
                )

            return repo.create(name)

        finally:
            session.close()

    def update_role(
        self,
        role_id: int,
        name: str,
    ):

        session = SessionLocal()

        try:

            repo = RoleRepository(session)

            role = repo.get_by_id(role_id)

            if not role:
                raise ValueError(
                    "Role tidak ditemukan."
                )

            existing = repo.get_by_name(name)

            if existing and existing.id != role.id:
                raise ValueError(
                    f"Role '{name}' sudah ada."
                )

            return repo.update(
                role=role,
                name=name,
            )

        finally:
            session.close()

    def delete_role(
        self,
        role_id: int,
    ):

        session = SessionLocal()

        try:

            repo = RoleRepository(session)

            role = repo.get_by_id(role_id)

            if not role:
                raise ValueError(
                    "Role tidak ditemukan."
                )

            repo.delete(role)

        finally:
            session.close()