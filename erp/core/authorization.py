class Authorization:

    def __init__(self, permissions):

        self.permissions = set(
            permissions
        )

    def can(
        self,
        permission,
    ):

        return permission in self.permissions