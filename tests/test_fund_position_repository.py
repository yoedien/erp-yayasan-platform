from erp.database.session import SessionLocal
from erp.repositories.fund_position_repository import (
    FundPositionRepository,
)

session = SessionLocal()

try:

    repo = FundPositionRepository(session)

    data = repo.get_all()

    print("Jumlah Pos Dana :", len(data))

    for row in data:

        print(
            row.code,
            row.name,
            row.budget,
        )

finally:

    session.close()
