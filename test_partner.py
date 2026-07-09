from erp.database.session import SessionLocal
from erp.repositories.partner_repository import PartnerRepository

session = SessionLocal()

repo = PartnerRepository(session)

partners = repo.get_all()

print(f"Jumlah partner : {len(partners)}")

for partner in partners:
    print(
        partner.id,
        partner.code,
        partner.name,
        partner.partner_type,
    )

session.close()
