from .common import Unit
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Create = CRUDResponse[Unit]
Read = CRUDResponse[Unit]
Update = CRUDResponse[Unit]
List = ListResponse[Unit]
