from .base import BaseRepo
from database.models import Groups


class GroupsRepo(BaseRepo[Groups]):
    MODEL = Groups