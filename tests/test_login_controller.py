from erp.controllers import LoginController
from erp.database.session import SessionLocal

session = SessionLocal()

controller = LoginController(session)

success = controller.login(
    "admin",
    "admin123",
)

print("Login:", success)

if success:
    print(controller.current_user.username)
    print(controller.current_user.full_name)
    print(controller.current_user.role.name)

controller.logout()

print(controller.current_user)

session.close()