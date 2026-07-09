from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Numeric,
)

from sqlalchemy.orm import relationship

from erp.database.base import Base


class ProposalItem(Base):
    __tablename__ = "proposal_items"

    id = Column(
        Integer,
        primary_key=True,
    )

    proposal_id = Column(
        Integer,
        ForeignKey("proposals.id"),
        nullable=False,
    )

    item_name = Column(
        String(200),
        nullable=False,
    )

    specification = Column(
        String(500),
    )

    quantity = Column(
        Numeric(18, 2),
        default=1,
    )

    unit = Column(
        String(30),
    )

    unit_price = Column(
        Numeric(18, 2),
        default=0,
    )

    subtotal = Column(
        Numeric(18, 2),
        default=0,
    )

    notes = Column(
        String(500),
    )

    proposal = relationship(
        "Proposal",
        back_populates="items",
    )
