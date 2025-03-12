from pydantic import BaseModel
from schemas.auth.common import UserRole


class Update(BaseModel):
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None

    role: UserRole | None = None
    group_id: int | None = None
