from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, ForeignKey
from enum import IntEnum


class WorkType(IntEnum):
    HOMEWORK = 0
    PRACTICAL_WORK = 1
    LABORATORY_WORK = 2
    VERIFICATION_WORK = 3
    COURSE_WORK = 4


class MarkType(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Mark(Base):
    __tablename__ = "marks"

    discipline_id: Mapped[int] = mapped_column(ForeignKey("disciplines.id", ondelete="CASCADE"))
    student_id: Mapped[int] = mapped_column()
    work_type: Mapped[WorkType] = mapped_column()
    date: Mapped[Date] = mapped_column(Date)
    value: Mapped[MarkType] = mapped_column()
