from erp.auth.password import hash_password
from erp.database.session import SessionLocal
from erp.repositories.user_repository import UserRepository


class UserService:

    def get_users(self):

        session = SessionLocal()

        try:
            repo = UserRepository(session)

            return repo.get_all()

        finally:
            session.close()

    def get_by_username(self, username: str):

        session = SessionLocal()

        try:
            repo = UserRepository(session)

            return repo.get_by_username(username)

        finally:
            session.close()

    def create_user(
        self,
        username: str,
        password: str,
        full_name: str,
        role_id: int,
        unit_id: int,
    ):

        session = SessionLocal()

        try:

            repo = UserRepository(session)

            existing = repo.get_by_username(username)

            if existing:
                raise ValueError(
                    f"Username '{username}' sudah digunakan."
                )

            password_hash = hash_password(password)

            return repo.create(
                username=username,
                password_hash=password_hash,
                full_name=full_name,
                role_id=role_id,
                unit_id=unit_id,
            )

        finally:
            session.close()