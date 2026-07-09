from erp.database.session import SessionLocal
from erp.repositories.academic_year_repository import AcademicYearRepository

session = SessionLocal()

repo = AcademicYearRepository(session)

for item in repo.get_all():
    print(item.code, item.name)
