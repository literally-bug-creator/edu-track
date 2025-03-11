from pydantic import BaseModel


class Create(BaseModel):
    number: str
    track_id: int


class Update(BaseModel):
    number: str | None = None
    track_id: int | None = None