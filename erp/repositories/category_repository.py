from sqlalchemy import select

from erp.models import Category
from .base_repository import BaseRepository


class CategoryRepository(BaseRepository):

    def get_all(self):

        return self.session.scalars(
            select(Category)
            .order_by(Category.code)
        ).all()

    def get_by_id(
        self,
        category_id: int,
    ):

        return self.session.scalar(
            select(Category).where(
                Category.id == category_id
            )
        )

    def get_by_code(
        self,
        code: str,
    ):

        return self.session.scalar(
            select(Category).where(
                Category.code == code
            )
        )

    def create(
        self,
        code: str,
        name: str,
        description: str,
        is_active: bool,
    ):

        category = Category(
            code=code,
            name=name,
            description=description,
            is_active=is_active,
        )

        self.session.add(category)

        self.session.commit()

        self.session.refresh(category)

        return category

    def update(
        self,
        category,
        code: str,
        name: str,
        description: str,
        is_active: bool,
    ):

        category.code = code
        category.name = name
        category.description = description
        category.is_active = is_active

        self.session.commit()

        self.session.refresh(category)

        return category

    def delete(
        self,
        category,
    ):

        self.session.delete(category)

        self.session.commit()