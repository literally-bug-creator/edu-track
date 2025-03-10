from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class DisciplineGroup(Base):
    __tablename__ = "disciplines_groups"

    discipline_id: Mapped[int] = mapped_column(
        ForeignKey("disciplines.id"), primary_key=True
    )
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), primary_key=True)
