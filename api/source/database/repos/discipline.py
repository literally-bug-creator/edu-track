from .base import BaseRepo
from database.models import Discipline


class DisciplineRepo(BaseRepo):
    MODEL = Discipline
