from datetime import datetime
from pydantic import BaseModel, ConfigDict
from enum import IntEnum


class UserRole(IntEnum):
    ADMIN = 0
    TEACHER = 1
    STUDENT = 2


class User(BaseModel):  # TODO: Make NameStr for first_name, middle_name and last_name
    id: int
    email: str
    first_name: str
    middle_name: str
    last_name: str
    role: UserRole
    group_id: int | None

    model_config = ConfigDict(from_attributes=True)


class TokenPayload(User):
    exp: datetime
