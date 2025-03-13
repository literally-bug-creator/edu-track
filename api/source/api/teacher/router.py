from fastapi import APIRouter, Depends, status
from schemas.teacher import params, bodies, responses
from services.teacher import TeacherService
from schemas.auth.common import User, UserRole
from utils.auth import get_user_has_role, get_user_by_min_role

from .config import EPath, PREFIX


router = APIRouter(prefix=PREFIX, tags=["Teacher"])


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
    user: User = Depends(get_user_has_role([UserRole.ADMIN, UserRole.TEACHER])),
    service: TeacherService = Depends(TeacherService),
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
    body: bodies.Update,
    pms: params.Update = Depends(),
    user: User = Depends(get_user_by_min_role(UserRole.ADMIN)),
    service: TeacherService = Depends(TeacherService),
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
    service: TeacherService = Depends(TeacherService),
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
    service: TeacherService = Depends(TeacherService),
):
    return await service.list(pms, user)


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
    pms: params.List = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN, UserRole.TEACHER])),
    service: TeacherService = Depends(TeacherService),
):
    return await service.list_disciplines(pms, user)
