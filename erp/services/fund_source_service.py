from erp.database.session import SessionLocal

from erp.repositories.fund_source_repository import (
    FundSourceRepository,
)


class FundSourceService:

    # ==========================================
    # GET ALL
    # ==========================================

    def get_fund_sources(self):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            return repo.get_all()

        finally:

            session.close()

    # ==========================================
    # GET ACTIVE
    # ==========================================

    def get_active_fund_sources(self):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            return repo.get_active()

        finally:

            session.close()

    # ==========================================
    # GET BY ID
    # ==========================================

    def get_fund_source(
        self,
        fund_source_id,
    ):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            return repo.get_by_id(fund_source_id)

        finally:

            session.close()

    # ==========================================
    # GENERATE CODE
    # ==========================================

    def generate_code(self):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            items = repo.get_all()

            if not items:
                return "FS001"

            last_code = items[-1].code

            nomor = int(last_code[2:]) + 1

            return f"FS{nomor:03d}"

        finally:

            session.close()

    # ==========================================
    # CREATE
    # ==========================================

    def create_fund_source(
        self,
        **kwargs,
    ):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            if repo.get_by_code(kwargs["code"]):

                raise ValueError("Kode Sumber Dana sudah digunakan.")

            return repo.create(**kwargs)

        finally:

            session.close()

    # ==========================================
    # UPDATE
    # ==========================================

    def update_fund_source(
        self,
        fund_source_id,
        **kwargs,
    ):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            obj = repo.get_by_id(fund_source_id)

            if obj is None:

                raise ValueError("Sumber Dana tidak ditemukan.")

            exist = repo.get_by_code(kwargs["code"])

            if exist and exist.id != fund_source_id:

                raise ValueError("Kode Sumber Dana sudah digunakan.")

            obj.code = kwargs["code"]
            obj.academic_year_id = kwargs["academic_year_id"]
            obj.unit_id = kwargs["unit_id"]
            obj.name = kwargs["name"]
            obj.description = kwargs["description"]
            obj.is_active = kwargs["is_active"]

            repo.update(obj)

            return obj

        finally:

            session.close()

    # ==========================================
    # DELETE
    # ==========================================

    def delete_fund_source(
        self,
        fund_source_id,
    ):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            ok = repo.delete(fund_source_id)

            if not ok:

                raise ValueError("Sumber Dana tidak ditemukan.")

        finally:

            session.close()

    # ==========================================
    # SEARCH
    # ==========================================

    def search(
        self,
        keyword,
    ):

        session = SessionLocal()

        try:

            repo = FundSourceRepository(session)

            return repo.search(keyword)

        finally:

            session.close()
