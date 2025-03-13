from .common import Teacher
from schemas.discipline.common import Discipline
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Teacher]
Read = CRUDResponse[Teacher]
Update = CRUDResponse[Teacher]
List = ListResponse[Teacher]
ListDisciplines = ListResponse[Discipline]
ReadDisciplineAvgMark = CRUDResponse[float]
