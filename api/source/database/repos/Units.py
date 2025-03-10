from .base import BaseRepo
from database.models import Units


class UnitsRepo(BaseRepo[Units]):
    MODEL = Units
