from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models.role import Role


DEFAULT_ROLES = [
    "Super Admin",
    "Ketua Yayasan",
    "Bendahara Yayasan",
    "Lajnah Pendidikan",
    "Kepala Sekolah",
    "Guru",
    "Staff TU",
    "Kasir",
    "Humas",
]


def seed_roles():

    session = SessionLocal()

    try:

        for role_name in DEFAULT_ROLES:

            exists = session.scalar(
                select(Role).where(
                    Role.name == role_name
                )
            )

            if exists:
                continue

            session.add(
                Role(
                    name=role_name
                )
            )

        session.commit()

        print("Role Seeder selesai.")

    finally:

        session.close()