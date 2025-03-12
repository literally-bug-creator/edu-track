from database.repos import StudentRepo, MarkRepo, DisciplineGroupRepo
from fastapi import Depends, HTTPException, status
from schemas.auth.common import User, UserRole
from schemas.marks.common import Mark
from schemas.discipline.common import Discipline
from schemas.student import bodies, params, responses
from schemas.student.common import Student
# from utils.auth import get_user_by_min_role, get_user_has_role


class StudentService:
    def __init__(
        self,
        repo: StudentRepo = Depends(StudentRepo),
        mark_repo: MarkRepo = Depends(MarkRepo),
        disc_group_repo: DisciplineGroupRepo = Depends(DisciplineGroupRepo),
    ) -> None:
        self.repo = repo
        self.mark_repo = mark_repo
        self.disc_group_repo = disc_group_repo

    async def read(
        self,
        pms: params.Read,
        user: User,
    ) -> responses.Read:
        if (user.role == UserRole.STUDENT) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.STUDENT
            )
        ):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = Student.model_validate(model, from_attributes=True)
        return responses.Read(item=scheme)

    async def update(
        self,
        pms: params.Update,
        body: bodies.Update,
        user: User,
    ) -> responses.Update:
        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.STUDENT
            )
        ):
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        upd_model = await self.repo.update(model, **body.model_dump(exclude_none=True))

        if upd_model is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = Student.model_validate(upd_model, from_attributes=True)
        return responses.Update(item=scheme)

    async def delete(
        self,
        pms: params.Delete,
        user: User,
    ) -> None:
        if not (
            model := await self.repo.filter_one(
                **pms.model_dump(), role=UserRole.STUDENT
            )
        ):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        await self.repo.delete(model)

    async def list(
        self,
        pms: params.List,
        user: User,
    ) -> responses.List:
        items, total = await self.repo.list(params=pms, role=UserRole.STUDENT)
        return responses.List(
            items=[Student.model_validate(obj, from_attributes=True) for obj in items],
            total=total,
        )

    async def list_marks(
        self,
        pms: params.ListMarks,
        user: User,
    ) -> responses.ListMarks:
        if (user.role == UserRole.STUDENT) and (user.id != pms.student_id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (await self.repo.filter_one(id=pms.student_id)):
            return responses.ListMarks(
                items=[],
                total=0,
            )

        items, total = await self.mark_repo.list(
            params=pms,
            student_id=pms.student_id,
            **pms.filters.model_dump(exclude_none=True),
        )
        return responses.ListMarks(
            items=[Mark.model_validate(obj, from_attributes=True) for obj in items],
            total=total,
        )
    
    async def list_disciplines(
        self,
        pms: params.ListDisciplines,
        user: User,
    ) -> responses.ListDisciplines:
        if (user.role == UserRole.STUDENT) and (user.id != pms.student_id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        
        if not (student := await self.repo.filter_one(id=pms.student_id)):
            return responses.ListDisciplines(items=[], total=0)

        items, total = await self.disc_group_repo.list(
            params=pms,
            group_id=student.group_id,
        )
        return responses.ListDisciplines(
            items=[Discipline.model_validate(obj, from_attributes=True) for obj in items],
            total=total,
        )
