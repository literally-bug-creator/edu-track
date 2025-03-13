from .common import Teacher
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Teacher]
Read = CRUDResponse[Teacher]
Update = CRUDResponse[Teacher]
List = ListResponse[Teacher]

