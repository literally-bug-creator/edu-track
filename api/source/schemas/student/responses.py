from .common import Student
from schemas.mark.common import MarksDistribution, AvgMarkByDate, ExtendedMark
from schemas.discipline.common import Discipline, DisciplineMarksAvg
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Student]
Read = CRUDResponse[Student]
ReadMarksDistribution = CRUDResponse[MarksDistribution]
Update = CRUDResponse[Student]
List = ListResponse[Student]
ListMarks = ListResponse[ExtendedMark]
ListDisciplines = ListResponse[Discipline]
ListDisciplinesMarksAvg = ListResponse[DisciplineMarksAvg]
ListMarksAvgByDate = ListResponse[AvgMarkByDate]
