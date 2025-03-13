from pydantic import BaseModel, Field
from enums import CourseNumber, SemesterNumber


class Create(BaseModel):
    name: str
    track_id: int
    course_number: CourseNumber = Field(default=CourseNumber.FIRST)
    semester_number: SemesterNumber = Field(default=SemesterNumber.FIRST)


class Update(BaseModel):
    name: str | None = None
    track_id: int | None = None
    course_number: CourseNumber = None
    semester_number: SemesterNumber = None
