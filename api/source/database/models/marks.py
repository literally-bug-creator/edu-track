from . import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, ForeignKey
from enum import IntEnum


class WorkType(IntEnum):
    HOMEWORK = 0
    PRACTICAL_WORK = 1
    LABORATORY_WORK = 2
    VERIFICATION_WORK = 3
    COURSE_WORK = 4


class Marks(Base):
    __tablename__ = "marks"

    discipline_id: Mapped[int] = mapped_column(ForeignKey("disciplines.id"))
    student_id: Mapped[int] = mapped_column()
    work_type: Mapped[WorkType] = mapped_column()
    date: Mapped[Date] = mapped_column(Date)
    value: Mapped[int] = mapped_column()
