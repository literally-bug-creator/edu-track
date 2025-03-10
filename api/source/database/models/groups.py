from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base, disciplines


class Groups(Base):
    __tablename__ = "groups"

    number: Mapped[str] = mapped_column()
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"))

    disciplines: Mapped[list["disciplines"]] = relationship(
        secondary="disciplines_groups", back_populates="groups"
    )
