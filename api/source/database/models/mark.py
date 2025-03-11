from .base import Base, BaseMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, ForeignKey
from .utils import MarkType, WorkType


class Mark(Base, BaseMixin):
    __tablename__ = "marks"

    discipline_id: Mapped[int] = mapped_column(ForeignKey("disciplines.id", ondelete="CASCADE"))
    student_id: Mapped[int] = mapped_column()
    work_type: Mapped[WorkType] = mapped_column()
    date: Mapped[Date] = mapped_column(Date)
    value: Mapped[MarkType] = mapped_column()
