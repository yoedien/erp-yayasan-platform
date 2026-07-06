from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models import Permission, Role, RolePermission


ROLE_PERMISSIONS = {
    "Super Admin": [
    "user.view",
    "user.create",
    "user.update",
    "user.delete",

    "role.view",
    "role.create",
    "role.update",
    "role.delete",

    "unit.view",
    "unit.create",
    "unit.update",
    "unit.delete",

    "proposal.create",
    "proposal.approve",

    "payment.create",
    "payment.approve",

    "report.view",

    "setting.manage",
],
    "Ketua Yayasan": [
        "proposal.approve",
        "payment.approve",
        "report.view",
    ],
    "Bendahara": [
        "payment.create",
        "report.view",
    ],
    "Kepala Sekolah": [
        "proposal.create",
        "report.view",
    ],
    "Operator": [
        "proposal.create",
    ],
}


def seed_role_permissions():

    session = SessionLocal()

    try:

        for role_name, permission_codes in ROLE_PERMISSIONS.items():

            role = session.scalar(
                select(Role).where(Role.name == role_name)
            )

            if role is None:
                continue

            for code in permission_codes:

                permission = session.scalar(
                    select(Permission).where(
                        Permission.code == code
                    )
                )

                if permission is None:
                    continue

                exists = session.scalar(
                    select(RolePermission).where(
                        RolePermission.role_id == role.id,
                        RolePermission.permission_id == permission.id,
                    )
                )

                if exists:
                    continue

                session.add(
                    RolePermission(
                        role_id=role.id,
                        permission_id=permission.id,
                    )
                )

        session.commit()

    finally:
        session.close()