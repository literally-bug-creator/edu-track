from pydantic import BaseModel
from enums import CourseNumber, SemesterNumber


class Discipline(BaseModel):
    id: int
    name: str
    track_id: int
    course_number: CourseNumber
    semester_number: SemesterNumber