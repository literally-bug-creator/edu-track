from pydantic_settings import BaseSettings
from pydantic import Field


class HostFilterMiddlewareSettings(BaseSettings):
    allowed_hosts: list[str] = Field(validation_alias="APP_ALLOWED_HOSTS")


def get_host_filter_middleware_settings() -> HostFilterMiddlewareSettings:
    return HostFilterMiddlewareSettings()  # type: ignore


__all__ = [
    "HostFilterMiddlewareSettings",
    "get_host_filter_middleware_settings",
]