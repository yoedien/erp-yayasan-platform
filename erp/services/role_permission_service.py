from erp.database.session import SessionLocal

from erp.repositories.permission_repository import (
    PermissionRepository,
)
from erp.repositories.role_repository import (
    RoleRepository,
)
from erp.repositories.role_permission_repository import (
    RolePermissionRepository,
)


class RolePermissionService:

    def get_role_permissions(
        self,
        role_id: int,
    ):

        session = SessionLocal()

        try:

            repo = RolePermissionRepository(
                session
            )

            return repo.get_by_role(
                role_id
            )

        finally:

            session.close()

    def save_permissions(
        self,
        role_id: int,
        permission_ids: list[int],
    ):

        session = SessionLocal()

        try:

            role_repo = RoleRepository(
                session
            )

            role = role_repo.get_by_id(
                role_id
            )

            if not role:

                raise ValueError(
                    "Role tidak ditemukan."
                )

            repo = RolePermissionRepository(
                session
            )

            current = repo.get_by_role(
                role_id
            )

            current_ids = {
                x.permission_id
                for x in current
            }

            selected_ids = set(
                permission_ids
            )

            # =========================
            # Hapus yang tidak dipilih
            # =========================

            for item in current:

                if (
                    item.permission_id
                    not in selected_ids
                ):

                    repo.delete(item)

            # =========================
            # Tambahkan yang baru
            # =========================

            for permission_id in selected_ids:

                if (
                    permission_id
                    not in current_ids
                ):

                    repo.create(
                        role_id=role_id,
                        permission_id=permission_id,
                    )

        finally:

            session.close()

    def get_all_permissions(self):

        session = SessionLocal()

        try:

            repo = PermissionRepository(
                session
            )

            return repo.get_all()

        finally:

            session.close()

    def get_all_roles(self):

        session = SessionLocal()

        try:

            repo = RoleRepository(
                session
            )

            return repo.get_all()

        finally:

            session.close()