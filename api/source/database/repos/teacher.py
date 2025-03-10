from .base import BaseRepo
from database.models import Teacher


class TeacherRepo(BaseRepo):
    MODEL = Teacher
