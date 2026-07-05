from erp.models import *

from .base import Base
from .engine import engine


def create_database():
    Base.metadata.create_all(bind=engine)
    print("Database berhasil dibuat.")


if __name__ == "__main__":
    create_database()