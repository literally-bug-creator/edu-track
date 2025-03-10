from .base import BaseRepo
from database.models import DisciplinesTeachers


class DisciplinesTeachersRepo(BaseRepo[DisciplinesTeachers]):
    MODEL = DisciplinesTeachers
