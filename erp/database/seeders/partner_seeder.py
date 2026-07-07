from erp.models import Partner
from erp.core.enums import PartnerType


def seed(session):

    if session.query(Partner).count():
        return

    data = [

        Partner(
            code="P00001",
            name="CV Maju Jaya",
            partner_type=PartnerType.SUPPLIER.value,
            city="Tulungagung",
            is_active=True,
        ),

        Partner(
            code="P00002",
            name="PT Telkom Indonesia",
            partner_type=PartnerType.VENDOR.value,
            city="Tulungagung",
            is_active=True,
        ),

        Partner(
            code="P00003",
            name="Bank Syariah Indonesia",
            partner_type=PartnerType.BANK.value,
            city="Tulungagung",
            is_active=True,
        ),
    ]

    session.add_all(data)

    session.commit()