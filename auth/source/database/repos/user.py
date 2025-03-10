from .base import BaseRepo
from database.models.user import User


class UserRepo(BaseRepo):
    MODEL = User