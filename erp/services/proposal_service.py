from datetime import datetime

from erp.models import Proposal
from erp.repositories.proposal_repository import (
    ProposalRepository,
)


class ProposalService:

    def __init__(self, session):

        self.session = session

        self.repository = ProposalRepository(session)

    def generate_number(self):

        today = datetime.now()

        prefix = f"PB-" f"{today.year}" f"{today.month:02d}-"

        proposals = self.repository.get_all()

        running_number = 1

        for proposal in proposals:

            if proposal.number.startswith(prefix):

                try:

                    number = int(proposal.number.split("-")[-1])

                    if number >= running_number:

                        running_number = number + 1

                except Exception:
                    pass

        return f"{prefix}" f"{running_number:04d}"

    def calculate_total(
        self,
        proposal,
    ):

        total = 0

        for item in proposal.items:

            item.subtotal = item.quantity * item.unit_price

            total += item.subtotal

        proposal.total = total

        return total

    def create(
        self,
        proposal: Proposal,
    ):

        if not proposal.number:

            proposal.number = self.generate_number()

        self.calculate_total(proposal)

        return self.repository.create(proposal)

    def update(
        self,
        proposal: Proposal,
    ):

        self.calculate_total(proposal)

        self.repository.update()

        return proposal

    def delete(
        self,
        proposal,
    ):

        self.repository.delete(proposal)
