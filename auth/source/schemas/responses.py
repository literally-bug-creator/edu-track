from pydantic import BaseModel
from shared.schemas.auth.common import User


class Me(User):
    ...


class Login(BaseModel):
    access_token: str
    token_type: str


class Register(User):
    ...
