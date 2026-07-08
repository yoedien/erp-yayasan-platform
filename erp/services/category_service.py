from erp.database.session import SessionLocal
from erp.repositories.category_repository import (
    CategoryRepository,
)


class CategoryService:

    def get_categories(self):

        session = SessionLocal()

        try:

            repo = CategoryRepository(session)

            return repo.get_all()

        finally:

            session.close()

    def create_category(
        self,
        code: str,
        name: str,
        description: str,
        is_active: bool,
    ):

        session = SessionLocal()

        try:

            repo = CategoryRepository(session)

            existing = repo.get_by_code(code)

            if existing:

                raise ValueError(
                    f"Kode '{code}' sudah digunakan."
                )

            return repo.create(
                code=code,
                name=name,
                description=description,
                is_active=is_active,
            )

        finally:

            session.close()

    def update_category(
        self,
        category_id: int,
        code: str,
        name: str,
        description: str,
        is_active: bool,
    ):

        session = SessionLocal()

        try:

            repo = CategoryRepository(session)

            category = repo.get_by_id(category_id)

            if not category:

                raise ValueError(
                    "Kategori tidak ditemukan."
                )

            existing = repo.get_by_code(code)

            if existing and existing.id != category.id:

                raise ValueError(
                    f"Kode '{code}' sudah digunakan."
                )

            return repo.update(
                category=category,
                code=code,
                name=name,
                description=description,
                is_active=is_active,
            )

        finally:

            session.close()

    def delete_category(
        self,
        category_id: int,
    ):

        session = SessionLocal()

        try:

            repo = CategoryRepository(session)

            category = repo.get_by_id(
                category_id
            )

            if not category:

                raise ValueError(
                    "Kategori tidak ditemukan."
                )

            repo.delete(category)

        finally:

            session.close()