from erp.auth import UserSession
from erp.services import AuthService


class LoginController:

    def __init__(self, session):
        self.auth_service = AuthService(session)
        self.user_session = UserSession()

    def login(
        self,
        username: str,
        password: str,
    ):

        user = self.auth_service.login(
            username,
            password,
        )

        if user is None:
            return False

        self.user_session.login(user)

        return True

    def logout(self):
        self.user_session.logout()

    @property
    def current_user(self):
        return self.user_session.user