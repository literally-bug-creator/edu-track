from database.repos import DisciplineRepo
from fastapi import Depends, HTTPException, status
from schemas.discipline import bodies, params, responses
from schemas.discipline.common import Discipline


class DisciplineService:
    def __init__(
        self,
        repo: DisciplineRepo = Depends(DisciplineRepo),
    ) -> None:
        self.repo = repo

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
