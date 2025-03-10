from .user import User
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Student(User):
    __tablename__ = "students"
    group_id = Mapped[int] = mapped_column(
        ForeignKey("groups.id"), primary_key=True
    )