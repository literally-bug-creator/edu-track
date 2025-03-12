from fastapi import APIRouter, Depends, status
from schemas.student import params, bodies, responses
from services.student import StudentService
from schemas.auth.common import User, UserRole
from utils.auth import get_user_has_role, get_user_by_min_role

from .config import EPath, PREFIX


router = APIRouter(prefix=PREFIX, tags=["Student"])


@router.get(
    path=EPath.READ,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Read},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def read(
    pms: params.Read = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN, UserRole.STUDENT])),
    service: StudentService = Depends(StudentService),
):
    return await service.read(pms, user)


@router.patch(
    path=EPath.UPDATE,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Update},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def update(
    pms: params.Update = Depends(),
    body: bodies.Update = Depends(),
    user: User = Depends(get_user_by_min_role(UserRole.ADMIN)),
    service: StudentService = Depends(StudentService),
):
    return await service.update(pms, body, user)


@router.delete(
    path=EPath.DELETE,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def delete(
    pms: params.Delete = Depends(),
    user: User = Depends(get_user_by_min_role(UserRole.ADMIN)),
    service: StudentService = Depends(StudentService),
):
    return await service.delete(pms, user)


@router.get(
    path=EPath.LIST,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.List},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def list(
    pms: params.List = Depends(),
    user: User = Depends(get_user_by_min_role(UserRole.ADMIN)),
    service: StudentService = Depends(StudentService),
):
    return await service.list(pms, user)


@router.get(
    path=EPath.LIST_MARKS,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.ListMarks},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def list_marks(
    pms: params.ListMarks = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN, UserRole.STUDENT])),
    service: StudentService = Depends(StudentService),
):
    return await service.list_marks(pms, user)


@router.get(
    path=EPath.LIST_DISCIPLINES,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.ListDisciplines},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def list_disciplines(
    pms: params.ListDisciplines = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN, UserRole.STUDENT])),
    service: StudentService = Depends(StudentService),
):
    return await service.list_disciplines(pms, user)


@router.get(
    path=EPath.READ_MARKS_DISTRIBUTION,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.ReadMarksDistribution},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def read_marks_distribution(
    pms: params.ReadMarksDistribution = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN, UserRole.STUDENT])),
    service: StudentService = Depends(StudentService),
):
    return await service.read_marks_distribution(pms, user)
