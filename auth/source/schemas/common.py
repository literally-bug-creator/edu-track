from datetime import datetime
from shared.schemas.auth.common import User


class TokenPayload(User):
    exp: datetime