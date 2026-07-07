from erp.database.session import SessionLocal


class BaseService:

    repository_class = None

    def execute(self, callback):

        session = SessionLocal()

        try:

            repo = self.repository_class(session)

            return callback(repo)

        finally:

            session.close()