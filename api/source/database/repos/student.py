from .base import BaseRepo
from database.models.user import User


class StudentRepo(BaseRepo):
    MODEL = User
