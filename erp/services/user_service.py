from erp.database.session import SessionLocal
from erp.repositories.user_repository import UserRepository


class UserService:

    def get_all(self):

        session = SessionLocal()

        try:
            repo = UserRepository(session)

            return repo.get_all()

        finally:
            session.close()