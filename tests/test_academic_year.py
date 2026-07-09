from erp.database.session import SessionLocal
from erp.repositories.academic_year_repository import AcademicYearRepository

session = SessionLocal()

try:
    repo = AcademicYearRepository(session)

    data = repo.get_all()

    print(f"Jumlah Tahun Pelajaran: {len(data)}")

    for item in data:
        print(
            item.id,
            item.code,
            item.name,
            item.is_active,
        )

finally:
    session.close()
