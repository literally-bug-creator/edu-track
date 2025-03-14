from pydantic import BaseModel
from enums import CourseNumber, SemesterNumber


class Discipline(BaseModel):
    id: int
    name: str
    track_id: int
    course_number: CourseNumber
    semester_number: SemesterNumber


class DisciplineMarksAvg(BaseModel):
    discipline_id: int
    avg_marks: float


class DisciplineGroup(BaseModel):
    discipline_id: int
    group_id: int


class DisciplineTeacher(BaseModel):
    discipline_id: int
    teacher_id: int
