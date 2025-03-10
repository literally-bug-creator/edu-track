from .base import Base
from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column


class AuthorizedUserMixin:
    email: Mapped[str] = mapped_column(String(255), index=True)
    hashed_password: Mapped[bytes] = mapped_column()

    __table_args__ = (Index("email_index", "email", postgresql_using="hash"),)


class NamedUserMixin:
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()


class User(Base, NamedUserMixin, AuthorizedUserMixin):
    __tablename__ = "users"
