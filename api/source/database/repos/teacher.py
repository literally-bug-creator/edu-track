from .base import BaseRepo
from database.models.user import User


class TeacherRepo(BaseRepo):
    MODEL = User
