from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from . import Disciplines

class Groups(Base):
    __tablename__ = "groups"
    
    number: Mapped[str] = mapped_column()
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"))
    
    disciplines: Mapped[list["Disciplines"]] = relationship(secondary="disciplines_groups", back_populates="groups")