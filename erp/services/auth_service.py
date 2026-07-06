from erp.auth.password import verify_password
from erp.repositories.user_repository import UserRepository


class AuthService:

    def __init__(self, session):
        self.user_repository = UserRepository(session)

    def login(
        self,
        username: str,
        password: str,
    ):

        user = self.user_repository.get_by_username(
            username
        )

        if user is None:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        return user