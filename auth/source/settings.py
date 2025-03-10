from pydantic import Field
from pydantic_settings import BaseSettings


class AuthSettings(BaseSettings):
    algorithm: str = Field(default="RS256", validation_alias="JWT_ALGORITHM")
    private_key_path: str = Field(validation_alias="JWT_PRIVATE_KEY_PATH")
    public_key_path: str = Field(validation_alias="JWT_PUBLIC_KEY_PATH")
    token_lifetime: int = Field(validation_alias="JWT_TOKEN_LIFETIME")