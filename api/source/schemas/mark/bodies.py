from pydantic import BaseModel
from .common import WorkType, MarkType
from utils.dt import utcnow, datetime


class Create(BaseModel):
    discipline_id: int
    student_id: int
    work_type: WorkType
    type: MarkType
    date: datetime = utcnow()
