from schemas.auth.common import User
from schemas.common.crud import CRUDResponse
from schemas.common.list import ListResponse


Read = CRUDResponse[User]
Update = CRUDResponse[User]
List = ListResponse[User]
