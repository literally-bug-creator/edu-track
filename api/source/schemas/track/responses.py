from .common import Track
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Track]
Read = CRUDResponse[Track]
Update = CRUDResponse[Track]
List = ListResponse[Track]
