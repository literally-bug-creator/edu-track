from .base import BaseRepo
from database.models import Tracks


class TracksRepo(BaseRepo[Tracks]):
    MODEL = Tracks