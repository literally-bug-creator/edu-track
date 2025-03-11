from sqlalchemy import Index, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import EmailType

from .base import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        EmailType, index=True
    )  
    hashed_password: Mapped[bytes] = mapped_column()

    first_name: Mapped[str] = mapped_column(String(255))
    middle_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))

    __table_args__ = (Index("email_index", "email", postgresql_using="hash"),)
