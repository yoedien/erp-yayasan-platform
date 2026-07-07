from sqlalchemy import select

from erp.models import Unit
from .base_repository import BaseRepository


class UnitRepository(BaseRepository):

    def get_all(self):
        return self.session.scalars(
            select(Unit).order_by(Unit.id)
        ).all()

    def get_by_id(self, unit_id: int):
        return self.session.scalar(
            select(Unit).where(
                Unit.id == unit_id
            )
        )

    def get_by_code(self, code: str):
        return self.session.scalar(
            select(Unit).where(
                Unit.code == code
            )
        )

    def create(
        self,
        code: str,
        name: str,
    ):

        unit = Unit(
            code=code,
            name=name,
        )

        self.session.add(unit)
        self.session.commit()
        self.session.refresh(unit)

        return unit

    def update(
        self,
        unit,
        code: str,
        name: str,
    ):

        unit.code = code
        unit.name = name

        self.session.commit()
        self.session.refresh(unit)

        return unit

    def delete(self, unit):

        self.session.delete(unit)
        self.session.commit()