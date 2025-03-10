from .base import BaseRepo
from database.models import Mark


class MarkRepo(BaseRepo):
    MODEL = Mark
