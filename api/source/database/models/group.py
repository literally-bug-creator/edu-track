from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, BaseMixin


class Group(Base, BaseMixin):
    __tablename__ = "groups"

    number: Mapped[str] = mapped_column(String(255))
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id", ondelete="CASCADE"))
