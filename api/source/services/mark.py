from database.repos import (
    DisciplineGroupRepo,
    DisciplineTeacherRepo,
    MarkRepo,
    UserRepo,
)
from fastapi import Depends, HTTPException, status
from schemas.auth.common import User, UserRole
from schemas.mark import bodies, responses
from schemas.mark.common import Mark
from utils.auth import get_user_by_min_role


class MarkService:
    def __init__(
        self,
        repo: MarkRepo = Depends(MarkRepo),
        user_repo: UserRepo = Depends(UserRepo),
        disc_teacher_repo: DisciplineTeacherRepo = Depends(DisciplineTeacherRepo),
        disc_group_repo: DisciplineGroupRepo = Depends(DisciplineGroupRepo),
        user: User = Depends(get_user_by_min_role(UserRole.TEACHER)),
    ) -> None:
        self.repo = repo
        self.user_repo = user_repo
        self.disc_teacher_repo = disc_teacher_repo
        self.disc_group_repo = disc_group_repo
        self.user = user

    async def create(self, body: bodies.Create) -> responses.Create:
        student = await self.user_repo.get(body.student_id)

        if student is None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST)

        if (student.role != UserRole.STUDENT) or (student.group_id is None):
            raise HTTPException(status.HTTP_400_BAD_REQUEST)

        if self.user.role == UserRole.TEACHER:
            discipline = await self.disc_teacher_repo.filter_one(
                discipline_id=body.discipline_id,
                teacher_id=self.user.id,
            )

            if discipline is None:
                raise HTTPException(status.HTTP_400_BAD_REQUEST)

        group = await self.disc_group_repo.filter_one(
            discipline_id=body.discipline_id,
            group_id=student.group_id,
        )

        if group is None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST)

        if not (model := await self.repo.new(**body.model_dump())):
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)

        scheme = Mark.model_validate(model, from_attributes=True)
        return responses.Create(item=scheme)
