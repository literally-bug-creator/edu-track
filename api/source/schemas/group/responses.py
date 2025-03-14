from .common import Group
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Group]
Read = CRUDResponse[Group]
Update = CRUDResponse[Group]
List = ListResponse[Group]
