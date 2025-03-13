from fastapi import APIRouter, Depends, status
from schemas.discipline import params, bodies, responses
from services.discipline import DisciplineService
from schemas.auth.common import User, UserRole
from utils.auth import get_user_has_role

from .config import EPath, PREFIX


router = APIRouter(prefix=PREFIX, tags=["Discipline"])


@router.put(
    path=EPath.CREATE,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.Create},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def create(
    body: bodies.Create,
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.create(body)


@router.get(
    path=EPath.READ,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Read},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
async def read(
    pms: params.Read = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.read(pms)


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
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.update(pms, body)


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
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.delete(pms)


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
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.list(pms)


@router.put(
    path=EPath.CREATE_GROUP,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.CreateGroup},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def create_group(
    pms: params.CreateGroup,
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.create_group(pms)


@router.get(
    path=EPath.READ_GROUP,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.ReadGroup},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
async def read_group(
    pms: params.ReadGroup = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.read_group(pms)


@router.delete(
    path=EPath.DELETE_GROUP,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
async def delete_group(
    pms: params.DeleteGroup = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.delete_group(pms)


@router.put(
    path=EPath.CREATE_TEACHER,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.CreateTeacher},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def create_teacher(
    pms: params.CreateTeacher,
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.create_teacher(pms)


@router.get(
    path=EPath.READ_TEACHER,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.ReadTeacher},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
async def read_teacher(
    pms: params.ReadTeacher = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.read_teacher(pms)


@router.delete(
    path=EPath.DELETE_TEACHER,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
async def delete_teacher(
    pms: params.DeleteTeacher = Depends(),
    user: User = Depends(get_user_has_role([UserRole.ADMIN])),
    service: DisciplineService = Depends(DisciplineService),
):
    return await service.delete_teacher(pms)
