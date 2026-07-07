from erp.database.session import SessionLocal
from erp.repositories.permission_repository import PermissionRepository


class PermissionService:

    def get_permissions(self):

        session = SessionLocal()

        try:

            repo = PermissionRepository(session)

            return repo.get_all()

        finally:

            session.close()

    def create_permission(
        self,
        code: str,
        name: str,
        module: str,
        description: str = None,
    ):

        session = SessionLocal()

        try:

            repo = PermissionRepository(session)

            existing = repo.get_by_code(code)

            if existing:

                raise ValueError(
                    f"Permission '{code}' sudah ada."
                )

            return repo.create(
                code=code,
                name=name,
                module=module,
                description=description,
            )

        finally:

            session.close()

    def update_permission(
        self,
        permission_id: int,
        code: str,
        name: str,
        module: str,
        description: str = None,
    ):

        session = SessionLocal()

        try:

            repo = PermissionRepository(session)

            permission = repo.get_by_id(
                permission_id
            )

            if not permission:

                raise ValueError(
                    "Permission tidak ditemukan."
                )

            existing = repo.get_by_code(code)

            if (
                existing
                and existing.id != permission.id
            ):

                raise ValueError(
                    f"Permission '{code}' sudah ada."
                )

            return repo.update(
                permission=permission,
                code=code,
                name=name,
                module=module,
                description=description,
            )

        finally:

            session.close()

    def delete_permission(
        self,
        permission_id: int,
    ):

        session = SessionLocal()

        try:

            repo = PermissionRepository(session)

            permission = repo.get_by_id(
                permission_id
            )

            if not permission:

                raise ValueError(
                    "Permission tidak ditemukan."
                )

            repo.delete(permission)

        finally:

            session.close()