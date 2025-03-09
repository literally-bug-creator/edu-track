from .base import BaseRepo
from database.models import Marks


class MarksRepo(BaseRepo[Marks]):
    MODEL = Marks