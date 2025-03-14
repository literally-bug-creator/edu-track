from .common import Teacher
from schemas.discipline.common import Discipline
from schemas.group.common import Group
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse
from schemas.student.common import Student


Create = CRUDResponse[Teacher]
Read = CRUDResponse[Teacher]
Update = CRUDResponse[Teacher]
List = ListResponse[Teacher]
ListDisciplines = ListResponse[Discipline]
ReadDisciplineAvgMark = CRUDResponse[float]
ReadGroup = CRUDResponse[Group]
ListGroupStudents = ListResponse[Student]
