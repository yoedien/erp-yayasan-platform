from erp.repositories.role_repository import RoleRepository


class RoleService:

    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def create_role(self, name: str):
        existing = self.repository.get_by_name(name)

        if existing:
            raise ValueError(f"Role '{name}' sudah ada.")

        return self.repository.create(name)

    def get_roles(self):
        return self.repository.get_all()