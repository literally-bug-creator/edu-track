from .common import Discipline, DisciplineGroup, DisciplineTeacher
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Discipline]
Read = CRUDResponse[Discipline]
Update = CRUDResponse[Discipline]
List = ListResponse[Discipline]

CreateGroup = CRUDResponse[DisciplineGroup]
ReadGroup = CRUDResponse[DisciplineGroup]

CreateTeacher = CRUDResponse[DisciplineTeacher]
ReadTeacher = CRUDResponse[DisciplineTeacher]
