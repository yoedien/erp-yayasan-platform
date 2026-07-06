from erp.models.user import User


class UserSession:

    def __init__(self):
        self._user: User | None = None

    def login(self, user: User):
        self._user = user

    def logout(self):
        self._user = None

    @property
    def user(self):
        return self._user

    @property
    def is_authenticated(self):
        return self._user is not None