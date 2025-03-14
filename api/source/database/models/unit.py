from .base import Base, BaseMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Unit(Base, BaseMixin):
    __tablename__ = "units"

    name: Mapped[str] = mapped_column(String(255))
