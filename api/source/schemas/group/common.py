from pydantic import BaseModel


class Group(BaseModel):
    id: int
    number: str
    track_id: int
