from sqlalchemy import select

from erp.models import FundPosition


class FundPositionRepository:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return (
            self.session.execute(select(FundPosition).order_by(FundPosition.code))
            .scalars()
            .all()
        )

    def get_by_id(self, id):
        return self.session.get(
            FundPosition,
            id,
        )

    def get_by_source(self, fund_source_id):
        return (
            self.session.execute(
                select(FundPosition)
                .where(FundPosition.fund_source_id == fund_source_id)
                .order_by(FundPosition.code)
            )
            .scalars()
            .all()
        )

    def create(self, **kwargs):
        obj = FundPosition(**kwargs)

        self.session.add(obj)

        self.session.commit()

        self.session.refresh(obj)

        return obj

    def update(self, obj, **kwargs):

        for key, value in kwargs.items():
            setattr(obj, key, value)

        self.session.commit()

        self.session.refresh(obj)

        return obj

    def delete(self, obj):

        self.session.delete(obj)

        self.session.commit()
