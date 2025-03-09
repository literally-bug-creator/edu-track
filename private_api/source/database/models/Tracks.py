from . import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class Tracks(Base):
    __tablename__ = "tracks"
    
    name: Mapped[str] = mapped_column()
    unit_id: Mapped[int] = mapped_column(ForeignKey("units.id"))