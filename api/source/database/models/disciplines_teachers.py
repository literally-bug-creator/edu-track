from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class DisciplineTeachers(Base):
    __tablename__ = "disciplines_teachers"

    discipline_id: Mapped[int] = mapped_column(
        ForeignKey("disciplines.id"), primary_key=True
    )
    teacher_id: Mapped[int] = mapped_column()
