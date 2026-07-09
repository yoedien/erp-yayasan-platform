from erp.database.session import SessionLocal
from erp.services.authorization_service import AuthorizationService

session = SessionLocal()

try:
    service = AuthorizationService(session)

    permissions = service.get_permissions(1)

    print("Permissions Role ID 1:")
    print(permissions)

finally:
    session.close()
