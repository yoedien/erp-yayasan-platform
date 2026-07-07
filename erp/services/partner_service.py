from erp.database.session import SessionLocal
from erp.repositories.partner_repository import PartnerRepository


class PartnerService:

    def get_partners(self):

        session = SessionLocal()

        try:
            repo = PartnerRepository(session)

            return repo.get_all()

        finally:
            session.close()

    def create_partner(self, **kwargs):

        session = SessionLocal()

        try:

            repo = PartnerRepository(session)

            if repo.get_by_code(kwargs["code"]):
                raise ValueError(
                    "Kode Partner sudah digunakan."
                )

            return repo.create(**kwargs)

        finally:
            session.close()

    def update_partner(
        self,
        partner_id,
        **kwargs,
    ):

        session = SessionLocal()

        try:

            repo = PartnerRepository(session)

            partner = repo.get_by_id(partner_id)

            if not partner:
                raise ValueError(
                    "Partner tidak ditemukan."
                )

            return repo.update(
                partner,
                **kwargs,
            )

        finally:
            session.close()

    def delete_partner(
        self,
        partner_id,
    ):

        session = SessionLocal()

        try:

            repo = PartnerRepository(session)

            partner = repo.get_by_id(
                partner_id
            )

            if not partner:
                raise ValueError(
                    "Partner tidak ditemukan."
                )

            repo.delete(partner)

        finally:
            session.close()