from schemas.common.list import ListParams
from pydantic import BaseModel
from fastapi import Path


class Read(BaseModel):
    id: int = Path()


class Update(BaseModel):
    id: int = Path()


class Delete(BaseModel):
    id: int = Path()


class List(ListParams):
    pass


class CreateGroup(BaseModel):
    id: int = Path()
    group_id: int = Path()


class ReadGroup(BaseModel):
    id: int = Path()
    group_id: int = Path()


class DeleteGroup(BaseModel):
    id: int = Path()
    group_id: int = Path()


class ListGroups(BaseModel):
    id: int = Path()


class CreateTeacher(BaseModel):
    id: int = Path()
    teacher_id: int = Path()


class ReadTeacher(BaseModel):
    id: int = Path()
    teacher_id: int = Path()


class DeleteTeacher(BaseModel):
    id: int = Path()
    teacher_id: int = Path()


class ListTeachers(BaseModel):
    id: int = Path()
