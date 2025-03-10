from .base import Base, BaseMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String


class Track(Base, BaseMixin):
    __tablename__ = "tracks"

    name: Mapped[str] = mapped_column(String(255))
    unit_id: Mapped[int] = mapped_column(ForeignKey("units.id", ondelete="CASCADE"))
