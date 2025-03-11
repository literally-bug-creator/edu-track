from .common import Discipline
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Discipline]
Read = CRUDResponse[Discipline]
Update = CRUDResponse[Discipline]
List = ListResponse[Discipline]
