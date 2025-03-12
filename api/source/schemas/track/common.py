from pydantic import BaseModel


class Track(BaseModel):
    id: int
    name: str
    unit_id: int
