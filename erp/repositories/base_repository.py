from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):

    model = None

    def __init__(self, session: Session):

        self.session = session

    # ==========================
    # READ
    # ==========================

    def get_all(self):

        return self.session.scalars(
            select(self.model)
        ).all()

    def get_by_id(self, id_):

        return self.session.get(
            self.model,
            id_,
        )

    # ==========================
    # CREATE
    # ==========================

    def create(self, **kwargs):

        obj = self.model(**kwargs)

        self.session.add(obj)

        self.session.commit()

        self.session.refresh(obj)

        return obj

    # ==========================
    # UPDATE
    # ==========================

    def update(
        self,
        obj,
        **kwargs,
    ):

        for key, value in kwargs.items():

            setattr(
                obj,
                key,
                value,
            )

        self.session.commit()

        self.session.refresh(obj)

        return obj

    # ==========================
    # DELETE
    # ==========================

    def delete(self, obj):

        self.session.delete(obj)

        self.session.commit()