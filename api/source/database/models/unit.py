from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Unit(Base):
    __tablename__ = "units"

    name: Mapped[str] = mapped_column(String(255))
