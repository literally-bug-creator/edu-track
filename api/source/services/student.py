from database.repos import StudentRepo
from fastapi import Depends, HTTPException, status
from schemas.auth.common import User, UserRole
from schemas.student import bodies, params, responses
from schemas.student.common import Student
from utils.auth import get_permitted_user


class StudentService:
    def __init__(
        self,
        repo: StudentRepo = Depends(StudentRepo),
    ) -> None:
        self.repo = repo

    async def read(self, pms: params.Read) -> responses.Read:
        if not (model := await self.repo.filter_one(**pms.model_dump())):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = Student.model_validate(model, from_attributes=True)
        return responses.Read(item=scheme)

    async def update(
        self,
        pms: params.Update,
        body: bodies.Update,
        user: User = Depends(get_permitted_user(UserRole.ADMIN)),
    ) -> responses.Update:
        if not (model := await self.repo.filter_one(**pms.model_dump())):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        upd_model = await self.repo.update(model, **body.model_dump())

        if upd_model is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = Student.model_validate(upd_model, from_attributes=True)
        return responses.Update(item=scheme)

    async def delete(
        self,
        pms: params.Delete,
        user: User = Depends(get_permitted_user(UserRole.ADMIN)),
    ) -> None:
        if not (model := await self.repo.filter_one(**pms.model_dump())):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        await self.repo.delete(model)

    async def list(
        self,
        pms: params.List,
        user: User = Depends(get_permitted_user(UserRole.ADMIN)),
    ) -> responses.List:
        items, total = await self.repo.list(params=pms)
        return responses.List(
            items=[Student.model_validate(obj, from_attributes=True) for obj in items],
            total=total,
        )
