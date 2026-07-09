from sqlalchemy import select

from erp.auth.password import hash_password
from erp.database.session import SessionLocal
from erp.models import Role, Unit
from erp.repositories.user_repository import UserRepository

USERS = [
    {
        "username": "admin",
        "password": "admin123",
        "full_name": "Super Administrator",
        "role": "Super Admin",
        "unit": "YYS",
    },
    {
        "username": "ketua",
        "password": "123456",
        "full_name": "Ketua Yayasan",
        "role": "Ketua Yayasan",
        "unit": "YYS",
    },
    {
        "username": "bendahara",
        "password": "123456",
        "full_name": "Bendahara Yayasan",
        "role": "Bendahara Yayasan",
        "unit": "YYS",
    },
    {
        "username": "lajnah",
        "password": "123456",
        "full_name": "Lajnah Pendidikan",
        "role": "Lajnah Pendidikan",
        "unit": "YYS",
    },
    {
        "username": "kepalasd",
        "password": "123456",
        "full_name": "Kepala SD",
        "role": "Kepala Sekolah",
        "unit": "SD",
    },
    {
        "username": "kepalatk",
        "password": "123456",
        "full_name": "Kepala TK",
        "role": "Kepala Sekolah",
        "unit": "TK",
    },
    {
        "username": "guru_sd",
        "password": "123456",
        "full_name": "Guru SD",
        "role": "Guru",
        "unit": "SD",
    },
    {
        "username": "guru_tk",
        "password": "123456",
        "full_name": "Guru TK",
        "role": "Guru",
        "unit": "TK",
    },
]


def seed_users():

    session = SessionLocal()

    try:

        repo = UserRepository(session)

        for data in USERS:

            if repo.get_by_username(data["username"]):
                continue

            role = session.scalar(select(Role).where(Role.name == data["role"]))

            unit = session.scalar(select(Unit).where(Unit.code == data["unit"]))

            if role is None:
                print(f"Role {data['role']} tidak ditemukan.")
                continue

            if unit is None:
                print(f"Unit {data['unit']} tidak ditemukan.")
                continue

            repo.create(
                username=data["username"],
                password_hash=hash_password(data["password"]),
                full_name=data["full_name"],
                role_id=role.id,
                unit_id=unit.id,
            )

        session.commit()

        print("User Seeder selesai.")

    finally:

        session.close()


if __name__ == "__main__":
    seed_users()
