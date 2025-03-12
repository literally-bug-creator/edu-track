from pydantic import BaseModel
from enums import WorkType, MarkType
from datetime import datetime, timezone
from fastapi import Query


class Mark(BaseModel):
    discipline_id: int
    student_id: int
    work_type: WorkType
    type: MarkType
    date: datetime = datetime.now(timezone.utc)


class MarkFilters(BaseModel):
    discipline_id: int | None = Query(None)
    work_type: WorkType | None = Query(None)
