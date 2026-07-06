from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models.role import Role


ROLES = [
    "Super Admin",
    "Ketua Yayasan",
    "Bendahara",
    "Kepala Sekolah",
    "Operator",
]


def seed_roles():
    session = SessionLocal()

    try:
        for role_name in ROLES:

            exists = session.scalar(
                select(Role).where(
                    Role.name == role_name
                )
            )

            if exists:
                continue

            session.add(
                Role(
                    name=role_name,
                )
            )

        session.commit()

    finally:
        session.close()