from datetime import datetime
from shared.schemas.auth.common import User
from pydantic import BaseModel, ConfigDict


class BaseUser(BaseModel):
    email: str
    first_name: str
    middle_name: str
    last_name: str

    model_config = ConfigDict(from_attributes=True)


class User(BaseUser):
    id: int


class TokenPayload(User):
    exp: datetime
