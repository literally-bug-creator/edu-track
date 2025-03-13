from database.repos import TeacherRepo
from fastapi import Depends, HTTPException, status
from schemas.auth.common import User, UserRole
from schemas.teacher import bodies, params, responses
from schemas.teacher.common import Teacher


class TeacherService:
    def __init__(
        self,
        repo: TeacherRepo = Depends(TeacherRepo),
    ) -> None:
        self.repo = repo

    async def read(
        self,
        pms: params.Read,
        user: User,
    ) -> responses.Read:
        if (user.role == UserRole.TEACHER) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.TEACHER
            )
        ):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = Teacher.model_validate(model, from_attributes=True)
        return responses.Read(item=scheme)

    async def update(
        self,
        pms: params.Update,
        body: bodies.Update,
        user: User,
    ) -> responses.Update:
        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.TEACHER
            )
        ):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        upd_model = await self.repo.update(model, **body.model_dump(exclude_none=True))

        if upd_model is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = Teacher.model_validate(upd_model, from_attributes=True)
        return responses.Update(item=scheme)

    async def delete(
        self,
        pms: params.Delete,
        user: User,
    ) -> None:
        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.TEACHER
            )
        ):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        await self.repo.delete(model)

    async def list(
        self,
        pms: params.List,
        user: User,
    ) -> responses.List:
        items, total = await self.repo.list(params=pms, role=UserRole.TEACHER)
        return responses.List(
            items=[Teacher.model_validate(obj, from_attributes=True) for obj in items],
            total=total,
        )
