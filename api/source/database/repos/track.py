from .base import BaseRepo
from database.models import Track


class TrackRepo(BaseRepo):
    MODEL = Track
