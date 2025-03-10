from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from schemas import forms, responses
from services.auth import AuthService

from .config import EPath

app = FastAPI(title="EduTrack Auth API")
http_bearer = HTTPBearer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post(
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


@app.post(
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


@app.get(
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
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
    service: AuthService = Depends(AuthService),
):
    return await service.get_me(credentials)
