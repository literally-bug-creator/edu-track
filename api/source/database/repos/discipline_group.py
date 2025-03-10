from .base import BaseRepo
from database.models import DisciplineGroup


class DisciplineGroupRepo(BaseRepo):
    MODEL = DisciplineGroup
