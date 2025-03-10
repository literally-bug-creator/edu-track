from .base import BaseRepo
from database.models.user import Admin


class AdminRepo(BaseRepo):
    MODEL = Admin
