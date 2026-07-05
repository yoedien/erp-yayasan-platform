from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///erp_yayasan.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)