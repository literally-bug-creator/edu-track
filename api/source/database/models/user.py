from sqlalchemy import Index, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from schemas.auth.common import UserRole

from .base import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(index=True)
    hashed_password: Mapped[bytes] = mapped_column()

    first_name: Mapped[str] = mapped_column(String(255))
    middle_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))

    role: Mapped[UserRole] = mapped_column(default=UserRole.STUDENT, index=True)
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.id", ondelete="SET NULL"), index=True
    )

    __table_args__ = (Index("email_index", "email", postgresql_using="hash"),)
