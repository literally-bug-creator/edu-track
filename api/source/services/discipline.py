from database.repos import (
    DisciplineGroupRepo,
    DisciplineRepo,
    DisciplineTeacherRepo,
    GroupRepo,
)
from fastapi import Depends, HTTPException, status
from schemas.discipline import bodies, params, responses
from schemas.discipline.common import Discipline, DisciplineGroup, DisciplineTeacher


class DisciplineService:
    def __init__(
        self,
        repo: DisciplineRepo = Depends(DisciplineRepo),
        group_repo: GroupRepo = Depends(GroupRepo),
        discipline_group_repo: DisciplineGroupRepo = Depends(DisciplineGroupRepo),
        discipline_teacher_repo: DisciplineTeacherRepo = Depends(DisciplineTeacherRepo),
    ) -> None:
        self.repo = repo
        self.group_repo = group_repo
        self.discipline_group_repo = discipline_group_repo
        self.discipline_teacher_repo = discipline_teacher_repo

    async def create(self, body: bodies.Create) -> responses.Create:
        if not (model := await self.repo.new(**body.model_dump())):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = Discipline.model_validate(model, from_attributes=True)
        return responses.Create(item=scheme)

    async def read(self, pms: params.Read) -> responses.Read:
        if not (model := await self.repo.filter_one(**pms.model_dump())):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = Discipline.model_validate(model, from_attributes=True)
        return responses.Read(item=scheme)

    async def update(self, pms: params.Update, body: bodies.Update) -> responses.Update:
        if not (model := await self.repo.filter_one(**pms.model_dump())):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        upd_model = await self.repo.update(model, **body.model_dump(exclude_none=True))

        if upd_model is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = Discipline.model_validate(upd_model, from_attributes=True)
        return responses.Update(item=scheme)

    async def delete(self, pms: params.Delete) -> None:
        if not (model := await self.repo.filter_one(**pms.model_dump())):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        await self.repo.delete(model)

    async def list(self, pms: params.List) -> responses.List:
        items, total = await self.repo.list(params=pms)
        return responses.List(
            items=[
                Discipline.model_validate(obj, from_attributes=True) for obj in items
            ],
            total=total,
        )

    async def create_group(self, pms: params.CreateGroup) -> responses.CreateGroup:
        if not (await self.repo.filter_one(discipline_id=pms.id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        if not (await self.group_repo.get(pms.group_id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        discipline_group = await self.discipline_group_repo.filter_one(
            discipline_id=pms.id,
            group_id=pms.group_id,
        )

        if discipline_group is not None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST)

        discipline_group_model = await self.discipline_group_repo.new(
            discipline_id=pms.id,
            group_id=pms.group_id,
        )

        if discipline_group_model is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = DisciplineGroup.model_validate(
            discipline_group_model,
            from_attributes=True,
        )

        return responses.CreateGroup(item=scheme)

    async def read_group(self, pms: params.ReadGroup) -> responses.ReadGroup:
        model = await self.discipline_group_repo.filter_one(
            discipline_id=pms.id,
            group_id=pms.group_id,
        )

        if model is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = DisciplineGroup.model_validate(model, from_attributes=True)
        return responses.ReadGroup(item=scheme)

    async def delete_group(self, pms: params.DeleteGroup) -> None:
        model = await self.discipline_group_repo.filter_one(
            discipline_id=pms.id,
            group_id=pms.group_id,
        )

        if model is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        await self.discipline_group_repo.delete(model)

    async def create_teacher(self, pms: params.CreateTeacher) -> responses.CreateTeacher:
        if not (await self.repo.filter_one(discipline_id=pms.id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        if not (await self.discipline_teacher_repo.get(pms.teacher_id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        discipline_teacher = await self.discipline_teacher_repo.filter_one(
            discipline_id=pms.id,
            teacher_id=pms.teacher_id,
        )

        if discipline_teacher is not None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST)

        discipline_teacher_model = await self.discipline_teacher_repo.new(
            discipline_id=pms.id,
            teacher_id=pms.teacher_id,
        )

        if discipline_teacher_model is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = DisciplineTeacher.model_validate(
            discipline_teacher_model,
            from_attributes=True,
        )

        return responses.CreateTeacher(item=scheme)

    async def read_teacher(self, pms: params.ReadTeacher) -> responses.ReadTeacher:
        model = await self.discipline_group_repo.filter_one(
            discipline_id=pms.id,
            group_id=pms.group_id,
        )

        if model is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = DisciplineGroup.model_validate(model, from_attributes=True)
        return responses.ReadGroup(item=scheme)

    async def delete_teacher(self, pms: params.DeleteTeacher) -> None:
        model = await self.discipline_teacher_repo.filter_one(
            discipline_id=pms.id,
            teacher_id=pms.teacher_id,
        )

        if model is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        await self.discipline_group_repo.delete(model)
