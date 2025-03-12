from fastapi import APIRouter, Depends, status
from schemas.student import params, bodies, responses
from services.student import StudentService

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
    service: StudentService = Depends(StudentService),
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
    pms: params.Update = Depends(),
    body: bodies.Update = Depends(),
    service: StudentService = Depends(StudentService),
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
    service: StudentService = Depends(StudentService),
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
    service: StudentService = Depends(StudentService),
):
    return await service.list(pms)
