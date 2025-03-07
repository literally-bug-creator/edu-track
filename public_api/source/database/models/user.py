from .base import Base
from enum import IntEnum
from sqlalchemy.orm import Mapped, mapped_column


class UserRole(IntEnum):
    ADMIN = 0
    TEACHER = 1
    STUDENT = 2


class RoleUserMixin:
    role: Mapped[UserRole] = mapped_column()


class AuthorizedUserMixin:
    email: Mapped[str] = mapped_column(index=True)
    hashed_password: Mapped[bytes] = mapped_column()


class NamedUserMixin:
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()


class User(Base, NamedUserMixin, AuthorizedUserMixin, RoleUserMixin):
    __tablename__ = "users"
