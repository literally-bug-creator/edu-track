from pydantic import BaseModel
from enums import WorkType, MarkType
from fastapi import Query
from utils.dt import utcnow, datetime


class Mark(BaseModel):
    discipline_id: int
    student_id: int
    work_type: WorkType
    type: MarkType
    date: datetime = utcnow()


class MarksDistribution(BaseModel):
    items: dict[MarkType, int]


class MarkFilters(BaseModel):
    discipline_id: int | None = Query(None)
    work_type: WorkType | None = Query(None)


class AvgMarkByDate(BaseModel):
    date: datetime
    value: float
