from sqlalchemy import select

from erp.models import Partner
from .base_repository import BaseRepository


class PartnerRepository(BaseRepository):

    def get_all(self):
        return self.session.scalars(
            select(Partner).order_by(Partner.code)
        ).all()

    def get_by_id(self, partner_id: int):
        return self.session.get(
            Partner,
            partner_id,
        )

    def get_by_code(self, code: str):
        return self.session.scalar(
            select(Partner).where(
                Partner.code == code
            )
        )

    def create(self, **kwargs):

        partner = Partner(**kwargs)

        self.session.add(partner)
        self.session.commit()
        self.session.refresh(partner)

        return partner

    def update(self, partner, **kwargs):

        for key, value in kwargs.items():
            setattr(partner, key, value)

        self.session.commit()
        self.session.refresh(partner)

        return partner

    def delete(self, partner):

        self.session.delete(partner)

        self.session.commit()