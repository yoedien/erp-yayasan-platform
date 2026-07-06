from erp.database.session import SessionLocal
from erp.services import AuthService
from erp.auth import UserSession

session = SessionLocal()

auth = AuthService(session)
user_session = UserSession()

user = auth.login(
    "admin",
    "admin123",
)

user_session.login(user)

print(user_session.is_authenticated)
print(user_session.user.username)
print(user_session.user.full_name)
print(user_session.user.role.name)
print(user_session.user.unit.name)

user_session.logout()

print(user_session.is_authenticated)

session.close()