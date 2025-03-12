from .common import Student
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Student]
Read = CRUDResponse[Student]
Update = CRUDResponse[Student]
List = ListResponse[Student]
