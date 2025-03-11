from pydantic import BaseModel


class Update(BaseModel):
    name: str | None = None
