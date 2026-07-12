from sqlalchemy import select

from erp.models import FundSource

from sqlalchemy.orm import joinedload

class FundSourceRepository:

    def __init__(self, session):

        self.session = session

    # ==========================================
    # GET ALL
    # ==========================================

    def get_all(self):

        stmt = (
            select(FundSource)
            .options(
                joinedload(FundSource.academic_year),
                joinedload(FundSource.unit),
            )
            .order_by(FundSource.code)
        )

        return list(self.session.scalars(stmt))

    # ==========================================
    # GET ACTIVE
    # ==========================================

    def get_active(self):

        stmt = (
            select(FundSource)
            .where(FundSource.is_active == True)
            .order_by(FundSource.code)
        )

        return list(self.session.scalars(stmt))

    # ==========================================
    # GET BY ID
    # ==========================================

    def get_by_id(
        self,
        fund_source_id,
    ):

        return self.session.get(
            FundSource,
            fund_source_id,
        )

    # ==========================================
    # GET BY CODE
    # ==========================================

    def get_by_code(
        self,
        code,
    ):

        stmt = (
            select(FundSource)
            .options(
                joinedload(FundSource.academic_year),
                joinedload(FundSource.unit),
            )
            .order_by(FundSource.code)
        )

        return self.session.scalar(stmt)

    # ==========================================
    # SEARCH
    # ==========================================

    def search(
        self,
        keyword,
    ):

        stmt = (
            select(FundSource)
            .where(FundSource.name.ilike(f"%{keyword}%"))
            .order_by(FundSource.code)
        )

        return list(self.session.scalars(stmt))

    # ==========================================
    # CREATE
    # ==========================================

    def create(
        self,
        **kwargs,
    ):

        obj = FundSource(
            **kwargs,
        )

        self.session.add(obj)

        self.session.commit()

        return obj

    # ==========================================
    # UPDATE
    # ==========================================

    def update(
        self,
        obj,
    ):

        self.session.add(obj)

        self.session.commit()

        return obj

    # ==========================================
    # DELETE
    # ==========================================

    def delete(
        self,
        fund_source_id,
    ):

        obj = self.get_by_id(fund_source_id)

        if obj:

            self.session.delete(obj)

            self.session.commit()

            return True

        return False
