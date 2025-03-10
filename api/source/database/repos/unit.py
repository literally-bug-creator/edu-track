from .base import BaseRepo
from database.models import Unit


class UnitRepo(BaseRepo):
    MODEL = Unit
