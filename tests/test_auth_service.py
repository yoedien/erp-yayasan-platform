from erp.database.session import SessionLocal
from erp.services import AuthService


session = SessionLocal()

service = AuthService(session)

user = service.login(
    "admin",
    "admin123",
)

print(user)

session.close()