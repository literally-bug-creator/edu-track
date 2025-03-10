from .base import BaseRepo
from database.models.user import Student


class StudentRepo(BaseRepo):
    MODEL = Student
