from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Numeric,
    Text,
)

from sqlalchemy.orm import relationship

from erp.database.base import Base


class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(
        Integer,
        primary_key=True,
    )

    number = Column(
        String(30),
        unique=True,
        nullable=False,
    )

    proposal_date = Column(
        DateTime,
        default=datetime.utcnow,
    )

    unit_id = Column(
        Integer,
        ForeignKey("units.id"),
        nullable=False,
    )

    requester_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    partner_id = Column(
        Integer,
        ForeignKey("partners.id"),
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
    )

    total = Column(
        Numeric(18, 2),
        default=0,
    )

    status = Column(
        String(20),
        default="Draft",
    )

    notes = Column(
        Text,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    unit = relationship("Unit")
    requester = relationship("User")
    partner = relationship("Partner")
    category = relationship("Category")

    items = relationship(
        "ProposalItem",
        back_populates="proposal",
        cascade="all, delete-orphan",
    )
