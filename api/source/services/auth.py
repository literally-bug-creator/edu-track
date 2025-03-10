import aiofiles
import bcrypt
import jwt
from database.repos.user import UserRepo
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from schemas import forms, responses
from schemas.auth.common import User as UserScheme
from settings import AuthSettings


class AuthService:
    def __init__(
        self,
        repo: UserRepo = Depends(UserRepo),
    ) -> None:
        self.repo = repo
        self.settings = AuthSettings()  # type: ignore
        self.unauthorized_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    async def register(self, form: forms.Register) -> responses.Register:
        if await self.repo.filter_one(email=form.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        hashed_password = self._hash_password(form.password)
        user_model = await self.repo.new(
            **form.model_dump(exclude={"password"}), hashed_password=hashed_password
        )

        if user_model is None:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

        return responses.Register.model_validate(user_model)

    async def login(self, form: forms.Login) -> responses.Login:
        if not (user_model := await self.repo.filter_one(email=form.email)):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        if not self._is_password_valid(form.password, user_model.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        payload = UserScheme.model_validate(user_model).model_dump()
        print(payload)
        private_key = await self._read_key(self.settings.private_key_path)

        token = jwt.encode(
            payload,
            private_key,
            self.settings.algorithm,
        )

        return responses.Login(access_token=token, token_type="Bearer")

    async def get_me(self, credentials: HTTPAuthorizationCredentials) -> responses.Me:
        token = credentials.credentials
        public_key = await self._read_key(self.settings.public_key_path)

        try:
            payload = jwt.decode(token, public_key, [self.settings.algorithm])
            user_scheme: UserScheme = UserScheme.model_validate(payload)
        except jwt.InvalidTokenError:
            raise self.unauthorized_exception

        if not await self.repo.filter_one(**user_scheme.model_dump()):
            raise self.unauthorized_exception

        return responses.Me.model_validate(user_scheme.model_dump())

    def _hash_password(
        self,
        password: str,
    ) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def _is_password_valid(
        self,
        password: str,
        hashed_password: bytes,
    ) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password)

    async def _read_key(self, path: str) -> str:
        async with aiofiles.open(path, "r") as key_file:
            return await key_file.read()
