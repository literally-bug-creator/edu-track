from fastapi import APIRouter, Depends, status
from utils.auth import oauth2_bearer
from schemas.auth import forms, responses
from services.auth import AuthService

from .config import EPath, PREFIX


router = APIRouter(prefix=PREFIX, tags=["Auth"])
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl=PREFIX + EPath.LOGIN) # TODO: Some fixes for all-api auth


@router.post(
    path=EPath.REGISTER,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.Register},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def register(
    form: forms.Register = Depends(forms.register),
    service: AuthService = Depends(AuthService),
):
    return await service.register(form)


@router.post(
    path=EPath.LOGIN,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Login},
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_401_UNAUTHORIZED: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def login(
    form: forms.Login = Depends(forms.login),
    service: AuthService = Depends(AuthService),
):
    return await service.login(form)


@router.get(
    path=EPath.ME,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Me},
        status.HTTP_401_UNAUTHORIZED: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
        status.HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def get_me(
    token: str = Depends(oauth2_bearer),
    service: AuthService = Depends(AuthService),
):
    return await service.get_me(token)
