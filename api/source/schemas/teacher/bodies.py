from pydantic import BaseModel


class Update(BaseModel):
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
