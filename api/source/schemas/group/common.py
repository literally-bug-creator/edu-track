from pydantic import BaseModel


class Group(BaseModel):
    number: str
    track_id: int
