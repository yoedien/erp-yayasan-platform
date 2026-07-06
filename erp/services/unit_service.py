from erp.database.session import SessionLocal
from erp.repositories.unit_repository import UnitRepository


class UnitService:

    def get_units(self):

        session = SessionLocal()

        try:
            repo = UnitRepository(session)

            return repo.get_all()

        finally:
            session.close()

    def create_unit(
        self,
        code: str,
        name: str,
    ):

        session = SessionLocal()

        try:

            repo = UnitRepository(session)

            existing = repo.get_by_code(code)

            if existing:
                raise ValueError(
                    f"Unit '{code}' sudah ada."
                )

            return repo.create(
                code,
                name,
            )

        finally:
            session.close()