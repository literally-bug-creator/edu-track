from .base import Base, BaseMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String
from .utils import CourseNumber, SemesterNumber


class Discipline(Base, BaseMixin):
    __tablename__ = "disciplines"

    name: Mapped[str] = mapped_column(String(255))
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id", ondelete="CASCADE"))
    course_number: Mapped[CourseNumber] = mapped_column()  
    semester_number: Mapped[SemesterNumber] = mapped_column()  