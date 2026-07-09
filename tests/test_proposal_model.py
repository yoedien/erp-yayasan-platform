from erp.database.session import SessionLocal
from erp.models import Proposal

session = SessionLocal()

proposal = Proposal()

print(proposal)
