from pydantic import BaseModel
from enums import WorkType, MarkType
from datetime import datetime, timezone


class Mark(BaseModel):
    discipline_id: int
    student_id: int
    work_type: WorkType
    type: MarkType
    date: datetime = datetime.now(timezone.utc)
