from erp.database.session import SessionLocal
from erp.repositories.academic_year_repository import (
    AcademicYearRepository,
)


class AcademicYearService:

    # ==================================================
    # GET ALL
    # ==================================================

    def get_academic_years(self):

        session = SessionLocal()

        try:

            repo = AcademicYearRepository(session)

            return repo.get_all()

        finally:

            session.close()

    # ==================================================
    # GET BY ID
    # ==================================================

    def get_academic_year(self, academic_year_id):

        session = SessionLocal()

        try:

            repo = AcademicYearRepository(session)

            return repo.get_by_id(academic_year_id)

        finally:

            session.close()

    # ==================================================
    # GENERATE CODE
    # ==================================================

    def generate_code(self):

        session = SessionLocal()

        try:

            repo = AcademicYearRepository(session)

            years = repo.get_all()

            if not years:
                return "TP2526"

            last = years[0].code

            nomor = int(last[2:]) + 101

            return f"TP{nomor}"

        finally:

            session.close()

    # ==================================================
    # CREATE
    # ==================================================

    def create_academic_year(self, **kwargs):

        session = SessionLocal()

        try:

            repo = AcademicYearRepository(session)

            if repo.get_by_code(kwargs["code"]):

                raise ValueError(
                    "Kode Tahun Pelajaran sudah digunakan."
                )

            if kwargs["is_active"]:

                for item in repo.get_active():

                    item.is_active = False

                    repo.update(item)

            return repo.create(**kwargs)

        finally:

            session.close()

    def update_academic_year(
        self,
        academic_year_id,
        **kwargs,
    ):

        session = SessionLocal()

        try:

            repo = AcademicYearRepository(session)

            obj = repo.get_by_id(academic_year_id)

            if obj is None:

                raise ValueError("Tahun Pelajaran tidak ditemukan.")
            
            exist = repo.get_by_code(kwargs["code"])

            if exist and exist.id != academic_year_id:

                raise ValueError("Kode Tahun Pelajaran sudah digunakan.")

            obj.code = kwargs["code"]
            obj.name = kwargs["name"]
            obj.start_date = kwargs["start_date"]
            obj.end_date = kwargs["end_date"]
            obj.is_active = kwargs["is_active"]

            # hanya satu aktif
            if obj.is_active:

                for item in repo.get_active():

                    if item.id != obj.id:

                        item.is_active = False

                        repo.update(item)

            repo.update(obj)

            return obj

        finally:

            session.close()

    # ==================================================
    # DELETE
    # ==================================================

    def delete_academic_year(
        self,
        academic_year_id,
    ):

        session = SessionLocal()

        try:

            repo = AcademicYearRepository(session)

            ok = repo.delete(academic_year_id)

            if not ok:

                raise ValueError("Tahun Pelajaran tidak ditemukan.")

        finally:

            session.close()
