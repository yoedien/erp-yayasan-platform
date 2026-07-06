from sqlalchemy import select

from erp.auth.password import hash_password
from erp.database.session import SessionLocal
from erp.models import Role, Unit
from erp.repositories.user_repository import UserRepository


def seed_super_admin():
    session = SessionLocal()

    try:
        user_repo = UserRepository(session)

        # Cek apakah admin sudah ada
        if user_repo.get_by_username("admin"):
            print("Super Admin already exists.")
            return

        role = session.scalar(
            select(Role).where(Role.name == "Super Admin")
        )

        unit = session.scalar(
            select(Unit).where(Unit.code == "YYS")
        )

        if role is None:
            raise ValueError("Role 'Super Admin' tidak ditemukan.")

        if unit is None:
            raise ValueError("Unit 'YYS' tidak ditemukan.")

        user_repo.create(
            username="admin",
            password_hash=hash_password("admin123"),
            full_name="Super Administrator",
            role_id=role.id,
            unit_id=unit.id,
        )

        print("Super Admin created.")

    finally:
        session.close()