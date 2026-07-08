from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models import Category


DEFAULT_CATEGORIES = [

    ("OPS", "Operasional"),

    ("SAR", "Sarana"),

    ("ADM", "Administrasi"),

    ("KBM", "Kegiatan Belajar"),

    ("SOS", "Sosial"),

    ("INV", "Inventaris"),

    ("DKW", "Dakwah"),

]


def seed_categories():

    session = SessionLocal()

    try:

        print("Seeding Categories...")

        for code, name in DEFAULT_CATEGORIES:

            exists = session.scalar(

                select(Category).where(

                    Category.code == code

                )

            )

            if exists:

                continue

            session.add(

                Category(

                    code=code,

                    name=name,

                    description="",

                    is_active=True,

                )

            )

        session.commit()

        print("Category Seeder selesai.")

    finally:

        session.close()