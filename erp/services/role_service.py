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

    def create_role(self, name: str):

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