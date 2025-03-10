from .base import BaseRepo
from database.models import Admin


class AdminRepo(BaseRepo):
    MODEL = Admin
