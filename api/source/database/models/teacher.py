from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Teacher:
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
