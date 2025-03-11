from pydantic import BaseModel


class Create(BaseModel):
    name: str
    unit_id: int


class Update(BaseModel):
    name: str | None = None
    unit_id: int | None = None