from datetime import date

from erp.models import AcademicYear


def seed_academic_years(session):

    if session.query(AcademicYear).count():
        return

    session.add_all(
        [
            AcademicYear(
                code="2025",
                name="2025/2026",
                start_date=date(2025, 7, 1),
                end_date=date(2026, 6, 30),
                is_active=False,
            ),
            AcademicYear(
                code="2026",
                name="2026/2027",
                start_date=date(2026, 7, 1),
                end_date=date(2027, 6, 30),
                is_active=True,
            ),
        ]
    )

    session.commit()

    print("Academic Year Seeder selesai.")
