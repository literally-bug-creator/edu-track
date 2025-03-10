from .base import BaseRepo
from database.models.user import Teacher


class TeacherRepo(BaseRepo):
    MODEL = Teacher
