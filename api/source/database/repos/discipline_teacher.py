from .base import BaseRepo
from database.models import DisciplineTeacher


class DisciplineTeacherRepo(BaseRepo):
    MODEL = DisciplineTeacher
