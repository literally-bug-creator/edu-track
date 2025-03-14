from database.repos import (
    DisciplineGroupRepo,
    DisciplineRepo,
    DisciplineTeacherRepo,
    GroupRepo,
    MarkRepo,
    StudentRepo,
    TeacherRepo,
)
from fastapi import Depends, HTTPException, status
from schemas.auth.common import User, UserRole
from schemas.discipline.common import Discipline
from schemas.group.common import Group
from schemas.student.common import Student
from schemas.teacher import bodies, params, responses
from schemas.teacher.common import Teacher


class TeacherService:
    def __init__(
        self,
        repo: TeacherRepo = Depends(TeacherRepo),
        mark_repo: MarkRepo = Depends(MarkRepo),
        group_repo: GroupRepo = Depends(GroupRepo),
        students_repo: StudentRepo = Depends(StudentRepo),
        discip_repo: DisciplineRepo = Depends(DisciplineRepo),
        discip_teacher_repo: DisciplineTeacherRepo = Depends(DisciplineTeacherRepo),
        discip_group_repo: DisciplineGroupRepo = Depends(DisciplineGroupRepo),
    ) -> None:
        self.repo = repo
        self.mark_repo = mark_repo
        self.group_repo = group_repo
        self.students_repo = students_repo
        self.discip_repo = discip_repo
        self.discip_teacher_repo = discip_teacher_repo
        self.discip_group_repo = discip_group_repo

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

    async def list_disciplines(
        self,
        pms: params.ListDisciplines,
        user: User,
    ) -> responses.ListDisciplines:
        if (user.role == UserRole.TEACHER) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not (await self.repo.filter_one(id=pms.id)):
            return responses.ListDisciplines(
                items=[],
                total=0,
            )

        items, _ = await self.discip_teacher_repo.list(
            params=pms,
            teacher_id=pms.id,
        )

        disciplines = []

        for item in items:
            discipline = await self.discip_repo.get(item.discipline_id)

            if discipline is not None:
                disciplines.append(
                    Discipline.model_validate(discipline, from_attributes=True)
                )

        return responses.ListDisciplines(
            items=disciplines,
            total=len(disciplines),
        )

    async def read_discipline_avg_mark(
        self, pms: params.ReadDisciplineAvgMark, user: User
    ) -> responses.ReadDisciplineAvgMark:
        discipline = await self.discip_repo.get(pms.discipline_id)

        if discipline is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        if (user.role == UserRole.TEACHER) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if user.role == UserRole.TEACHER:
            if not await self.discip_teacher_repo.filter_one(teacher_id=user.id):
                raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        marks = await self.mark_repo.filter(discipline_id=pms.discipline_id)
        marks_value = 0
        total = 0

        for mark in marks:
            marks_value += mark.type.value
            total += 1

        avg_mark = 0
        if total > 0:
            avg_mark = marks_value / total

        return responses.ReadDisciplineAvgMark(item=avg_mark)

    async def read_group(
        self,
        pms: params.ReadGroup,
        user: User,
    ) -> responses.ReadGroup:
        if (user.role == UserRole.TEACHER) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        group = None
        items = await self.discip_group_repo.filter(group_id=pms.group_id)
        for item in items:
            disc_teacher = await self.discip_teacher_repo.filter_one(
                discipline_id=item.discipline_id,
            )

            if disc_teacher is None:
                continue

            if disc_teacher.teacher_id == pms.id:
                group = await self.group_repo.get(pms.group_id)
                break

        if group is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        scheme = Group.model_validate(group, from_attributes=True)
        return responses.ReadGroup(item=scheme)

    async def list_group_students(
        self,
        pms: params.ListGroupStudents,
        user: User,
    ) -> responses.ListGroupStudents:
        if (user.role == UserRole.TEACHER) and (user.id != pms.id):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        group = None
        items = await self.discip_group_repo.filter(group_id=pms.group_id)
        for item in items:
            disc_teacher = await self.discip_teacher_repo.filter_one(
                discipline_id=item.discipline_id,
            )

            if disc_teacher is None:
                continue

            if disc_teacher.teacher_id == pms.id:
                group = await self.group_repo.get(pms.group_id)
                break

        if group is None:
            return responses.ListGroupStudents(items=[], total=0)

        students, total = await self.students_repo.list(
            params=pms,
            group_id=pms.group_id,
        )

        items = [
            Student.model_validate(student, from_attributes=True)
            for student in students
        ]

        return responses.ListGroupStudents(
            items=items,
            total=total,
        )
