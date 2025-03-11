from pydantic import BaseModel


class Create(BaseModel):
    name: str


class Update(BaseModel):
    name: str | None = None