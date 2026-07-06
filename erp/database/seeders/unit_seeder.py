from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models.unit import Unit


UNITS = [
    ("YYS", "Yayasan"),
    ("TK", "TK"),
    ("SD", "SD"),
    ("SMP", "SMP"),
    ("SMA", "SMA"),
    ("SMK", "SMK"),
]


def seed_units():
    session = SessionLocal()

    try:

        for code, name in UNITS:

            exists = session.scalar(
                select(Unit).where(
                    Unit.code == code
                )
            )

            if exists:
                continue

            session.add(
                Unit(
                    code=code,
                    name=name,
                )
            )

        session.commit()

    finally:
        session.close()