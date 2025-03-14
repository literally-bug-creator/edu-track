from datetime import datetime
from pydantic import BaseModel
from enum import IntEnum


class UserRole(IntEnum):
    ADMIN = 0
    TEACHER = 1
    STUDENT = 2


class User(BaseModel):
    id: int
    username: str
    first_name: str
    middle_name: str
    last_name: str
    role: UserRole
    group_id: int | None


class TokenPayload(User):
    exp: datetime
