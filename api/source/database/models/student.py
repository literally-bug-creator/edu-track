from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Student:
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    group_id: Mapped[int | None] = mapped_column(
        ForeignKey("groups.id", ondelete="SET NULL"), nullable=True, default=None, primary_key=True
    )
