from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from . import Groups

class Disciplines(Base):
    __tablename__ = "disciplines"
    
    name: Mapped[str] = mapped_column()
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"))
    course_number: Mapped[int] = mapped_column()
    semester_number: Mapped[int] = mapped_column()
    
    groups: Mapped[list["Groups"]] = relationship(secondary="disciplines_groups", back_populates="disciplines")
    # teachers: Mapped[list["Teachers"]] = relationship(secondary="disciplines_teachers", back_populates="disciplines")