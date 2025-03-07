from .host import Host
from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class HostFilterMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        allowed_hosts: list[str] | None = None,
    ):
        super().__init__(app)
        self.allowed_hosts = [Host(host) for host in allowed_hosts or ["*"]]
        self.allow_any = any(host.is_any for host in self.allowed_hosts)

    async def dispatch(self, request: Request, call_next) -> Response:
        if not self.allow_any:
            ip = request.headers.get("X-Real-IP") or None \
                if not request.client else request.client.host
            if ip is None or not any(host.is_same(ip) for host in self.allowed_hosts):
                return JSONResponse({"detail": "Forbidden host"}, status.HTTP_403_FORBIDDEN)
        return await call_next(request)


__all__ = [
    "HostFilterMiddleware",
]
