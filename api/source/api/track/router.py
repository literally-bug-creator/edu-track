from fastapi import APIRouter, Depends, status
from schemas.track import params, bodies, responses
from services.track import TrackService

from .config import EPath, PREFIX


router = APIRouter(prefix=PREFIX, tags=["Track"])


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
    service: TrackService = Depends(TrackService),
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
    service: TrackService = Depends(TrackService),
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
    service: TrackService = Depends(TrackService),
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
    service: TrackService = Depends(TrackService),
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
    service: TrackService = Depends(TrackService),
):
    return await service.list(pms)
