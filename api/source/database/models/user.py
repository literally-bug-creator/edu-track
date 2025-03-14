from schemas.auth.common import UserRole
from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(index=True)
    hashed_password: Mapped[bytes] = mapped_column()

    first_name: Mapped[str] = mapped_column(String(255))
    middle_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))

    role: Mapped[UserRole] = mapped_column(default=UserRole.STUDENT, index=True)
    group_id: Mapped[int | None] = mapped_column(
        ForeignKey("groups.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
        default=None,
    )

    __table_args__ = (Index("username_index", "username", postgresql_using="hash"),)
