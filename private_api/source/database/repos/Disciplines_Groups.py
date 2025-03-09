from .base import BaseRepo
from database.models import DisciplinesGroups


class DisciplinesGroupsRepo(BaseRepo[DisciplinesGroups]):
    MODEL = DisciplinesGroups
    