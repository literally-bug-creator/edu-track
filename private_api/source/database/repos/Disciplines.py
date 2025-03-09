from .base import BaseRepo
from database.models import Disciplines


class DisciplinesRepo(BaseRepo[Disciplines]):
    MODEL = Disciplines