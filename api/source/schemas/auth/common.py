from datetime import datetime
from pydantic import BaseModel, ConfigDict
from enum import IntEnum


class BaseUser(BaseModel):
    email: str
    first_name: str
    middle_name: str
    last_name: str

    model_config = ConfigDict(from_attributes=True)


class User(BaseUser):
    id: int


class UserRole(IntEnum):
    ADMIN = 0
    TEACHER = 1
    STUDENT = 2


class TokenPayload(User):
    exp: datetime
