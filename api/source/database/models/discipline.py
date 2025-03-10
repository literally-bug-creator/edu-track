from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String


class Discipline(Base):
    __tablename__ = "disciplines"

    name: Mapped[str] = mapped_column(String(255))
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id", ondelete="CASCADE"))
    course_number: Mapped[int] = mapped_column()  # TODO: Make enum for it
    semester_number: Mapped[int] = mapped_column()  # TODO: Make enum for it