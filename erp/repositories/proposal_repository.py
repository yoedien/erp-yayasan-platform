from sqlalchemy import select
from sqlalchemy.orm import joinedload

from erp.models import Proposal


class ProposalRepository:

    def __init__(self, session):
        self.session = session

    def get_all(self):

        stmt = (
            select(Proposal)
            .options(
                joinedload(Proposal.unit),
                joinedload(Proposal.requester),
                joinedload(Proposal.partner),
                joinedload(Proposal.category),
                joinedload(Proposal.items),
            )
            .order_by(Proposal.id.desc())
        )

        return list(self.session.scalars(stmt).unique().all())

    def get_by_id(
        self,
        proposal_id: int,
    ):

        stmt = (
            select(Proposal)
            .options(
                joinedload(Proposal.items),
                joinedload(Proposal.unit),
                joinedload(Proposal.requester),
                joinedload(Proposal.partner),
                joinedload(Proposal.category),
            )
            .where(Proposal.id == proposal_id)
        )

        return self.session.scalar(stmt)

    def get_by_number(
        self,
        number: str,
    ):

        stmt = select(Proposal).where(Proposal.number == number)

        return self.session.scalar(stmt)

    def create(
        self,
        proposal: Proposal,
    ):

        self.session.add(proposal)
        self.session.commit()
        self.session.refresh(proposal)

        return proposal

    def update(self):

        self.session.commit()

    def delete(
        self,
        proposal: Proposal,
    ):

        self.session.delete(proposal)
        self.session.commit()
