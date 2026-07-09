from erp.database.session import SessionLocal
from erp.repositories.user_repository import UserRepository

session = SessionLocal()

repo = UserRepository(session)

users = repo.get_all()

print(f"Jumlah user : {len(users)}")

for user in users:
    print(
        user.id,
        user.username,
        user.full_name,
    )
