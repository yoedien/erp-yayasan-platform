from datetime import date

from erp.database.session import SessionLocal
from erp.models import (
    Proposal,
    AcademicYear,
    FundSource,
    FundPosition,
    Unit,
    User,
    Partner,
    Category,
)

session = SessionLocal()

try:

    academic_year = session.query(AcademicYear).first()
    fund_source = session.query(FundSource).first()
    fund_position = session.query(FundPosition).first()
    unit = session.query(Unit).first()
    requester = session.query(User).first()
    partner = session.query(Partner).first()
    category = session.query(Category).first()

    if not academic_year:
        print("Academic Year belum ada.")
        exit()

    if not fund_source:
        print("Fund Source belum ada.")
        exit()

    if not fund_position:
        print("Fund Position belum ada.")
        exit()

    if not unit:
        print("Unit belum ada.")
        exit()

    if not requester:
        print("User belum ada.")
        exit()

    if not partner:
        print("Partner belum ada.")
        exit()

    if not category:
        print("Category belum ada.")
        exit()

    proposal = Proposal(
        number="TEST-0001",
        proposal_date=date.today(),
        unit_id=unit.id,
        requester_id=requester.id,
        partner_id=partner.id,
        academic_year_id=academic_year.id,
        fund_source_id=fund_source.id,
        fund_position_id=fund_position.id,
        category_id=category.id,
        priority="Normal",
        status="Draft",
        notes="Proposal Test",
        total=100000,
    )

    session.add(proposal)
    session.commit()

    proposal = session.query(Proposal).filter_by(number="TEST-0001").first()

    print("=" * 40)
    print("Proposal berhasil dibuat")
    print("=" * 40)

    print("Nomor           :", proposal.number)
    print("Tahun Pelajaran :", proposal.academic_year.name)
    print("Sumber Dana     :", proposal.fund_source.name)
    print("Pos Dana        :", proposal.fund_position.name)
    print("Kategori        :", proposal.category.name)
    print("Supplier        :", proposal.partner.name)
    print("Pemohon         :", proposal.requester.full_name)
    print("Unit            :", proposal.unit.name)
    print("Total           :", proposal.total)

finally:

    session.rollback()

    proposal = session.query(Proposal).filter_by(number="TEST-0001").first()

    if proposal:
        session.delete(proposal)
        session.commit()

    session.close()
