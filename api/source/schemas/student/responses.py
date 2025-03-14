from .common import Student
from schemas.mark.common import Mark, MarksDistribution, AvgMarkByDate
from schemas.discipline.common import Discipline, DisciplineMarksAvg
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Student]
Read = CRUDResponse[Student]
ReadMarksDistribution = CRUDResponse[MarksDistribution]
Update = CRUDResponse[Student]
List = ListResponse[Student]
ListMarks = ListResponse[Mark]
ListDisciplines = ListResponse[Discipline]
ListDisciplinesMarksAvg = ListResponse[DisciplineMarksAvg]
ListMarksAvgByDate = ListResponse[AvgMarkByDate]
