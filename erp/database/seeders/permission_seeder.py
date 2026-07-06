from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models.permission import Permission

PERMISSIONS = [
    # User
    ("user.view", "Lihat User", "User"),
    ("user.create", "Tambah User", "User"),
    ("user.update", "Ubah User", "User"),
    ("user.delete", "Hapus User", "User"),

    # Role
    ("role.view", "Lihat Role", "Role"),
    ("role.create", "Tambah Role", "Role"),
    ("role.update", "Ubah Role", "Role"),
    ("role.delete", "Hapus Role", "Role"),

    # Unit
    ("unit.view", "Lihat Unit", "Unit"),
    ("unit.create", "Tambah Unit", "Unit"),
    ("unit.update", "Ubah Unit", "Unit"),
    ("unit.delete", "Hapus Unit", "Unit"),
]


def seed_permissions():
    session = SessionLocal()

    try:
        for code, name, module in PERMISSIONS:

            exists = session.scalar(
                select(Permission).where(
                    Permission.code == code
                )
            )

            if exists:
                continue

            session.add(
                Permission(
                    code=code,
                    name=name,
                    module=module,
                    description=None,
                )
            )

        session.commit()

    finally:
        session.close()