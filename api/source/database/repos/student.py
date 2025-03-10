from .base import BaseRepo
from database.models import Student


class StudentRepo(BaseRepo):
    MODEL = Student
