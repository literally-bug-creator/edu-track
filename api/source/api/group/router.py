from fastapi import APIRouter, Depends, status
from schemas.group import params, bodies, responses
from services.group import GroupService

from .config import EPath, PREFIX


router = APIRouter(prefix=PREFIX, tags=["Group"])


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
    service: GroupService = Depends(GroupService),
):
    return await service.create(body)


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
    service: GroupService = Depends(GroupService),
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
    service: GroupService = Depends(GroupService),
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
    service: GroupService = Depends(GroupService),
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
    service: GroupService = Depends(GroupService),
):
    return await service.list(pms)
