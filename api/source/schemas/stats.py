from pydantic import BaseModel, model_validator
from datetime import date
from .utils import WorkType, CourseNumber, SemesterNumber


class BaseFilter(BaseModel):
    course: CourseNumber | None = None
    semester: SemesterNumber | None = None
    discipline_id: int | None = None
    period_start: date | None = None
    period_end: date | None = None

    @model_validator(mode="after")
    def check_period(self):
        if self.period_start and self.period_end:
            if self.period_end < self.period_start:
                raise ValueError("Конец периода должен быть после начала")
        return self


class MarkFilter(BaseFilter):
    work_type: WorkType | None = None


class AverageFilter(BaseFilter): ...
