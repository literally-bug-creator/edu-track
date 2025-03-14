from fastapi import APIRouter, Depends, status
from schemas.mark import bodies, responses
from services.mark import MarkService

from .config import PREFIX, EPath

router = APIRouter(prefix=PREFIX, tags=["Mark"])


@router.put(
    path=EPath.CREATE,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.Create},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def create(
    body: bodies.Create,
    service: MarkService = Depends(MarkService),
):
    return await service.create(body)
