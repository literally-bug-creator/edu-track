from .base import Base, BaseMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from enums import MarkType, WorkType
from utils.dt import utcnow, datetime


class Mark(Base, BaseMixin):
    __tablename__ = "marks"

    discipline_id: Mapped[int] = mapped_column(
        ForeignKey("disciplines.id", ondelete="CASCADE")
    )
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    work_type: Mapped[WorkType] = mapped_column()
    type: Mapped[MarkType] = mapped_column()
    date: Mapped[datetime] = mapped_column(default=utcnow)
