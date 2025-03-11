from pydantic import BaseModel


class Track(BaseModel):
    name: str
    unit_id: int
