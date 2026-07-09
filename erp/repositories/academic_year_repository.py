from sqlalchemy import select

from erp.models import AcademicYear


class AcademicYearRepository:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        stmt = select(AcademicYear).order_by(AcademicYear.code.desc())

        return list(self.session.scalars(stmt))

    def get_active(self):
        stmt = (
            select(AcademicYear)
            .where(AcademicYear.is_active == True)
            .order_by(AcademicYear.code.desc())
        )

        return list(self.session.scalars(stmt))

    def get_by_id(self, academic_year_id):

        return self.session.get(
            AcademicYear,
            academic_year_id,
        )

    def create(
        self,
        code,
        name,
        start_date,
        end_date,
        is_active=True,
    ):

        obj = AcademicYear(
            code=code,
            name=name,
            start_date=start_date,
            end_date=end_date,
            is_active=is_active,
        )

        self.session.add(obj)
        self.session.commit()

        return obj

    def update(self, obj):

        self.session.add(obj)
        self.session.commit()

        return obj

    def delete(self, academic_year_id):

        obj = self.get_by_id(academic_year_id)

        if obj:

            self.session.delete(obj)

            self.session.commit()

            return True

        return False
