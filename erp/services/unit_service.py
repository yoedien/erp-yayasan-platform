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
                code=code,
                name=name,
            )

        finally:
            session.close()

    def update_unit(
        self,
        unit_id: int,
        code: str,
        name: str,
    ):

        session = SessionLocal()

        try:

            repo = UnitRepository(session)

            unit = repo.get_by_id(unit_id)

            if not unit:
                raise ValueError(
                    "Unit tidak ditemukan."
                )

            existing = repo.get_by_code(code)

            if existing and existing.id != unit.id:
                raise ValueError(
                    f"Unit '{code}' sudah ada."
                )

            return repo.update(
                unit=unit,
                code=code,
                name=name,
            )

        finally:
            session.close()

    def delete_unit(
        self,
        unit_id: int,
    ):

        session = SessionLocal()

        try:

            repo = UnitRepository(session)

            unit = repo.get_by_id(unit_id)

            if not unit:
                raise ValueError(
                    "Unit tidak ditemukan."
                )

            repo.delete(unit)

        finally:
            session.close()