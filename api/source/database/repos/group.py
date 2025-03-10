from .base import BaseRepo
from database.models import Group


class GroupRepo(BaseRepo):
    MODEL = Group
