from database import Base as DBBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DBBase):  # type: ignore
    __abstract__ = True


class BaseMixin:
    id: Mapped[int] = mapped_column(primary_key=True, index=True)  # noqa
