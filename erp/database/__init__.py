from erp.database.base import Base
from erp.database.engine import engine

# Import semua model agar terdaftar di metadata
from erp.models import *


def init_database():
    Base.metadata.create_all(bind=engine)
    print("Database berhasil diinisialisasi.")


if __name__ == "__main__":
    init_database()