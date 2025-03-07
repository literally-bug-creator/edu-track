from fastapi import FastAPI
from shared.middlewares.host_filter import HostFilterMiddleware, get_host_filter_middleware_settings

app = FastAPI(title="EduTrack Private API")

app.add_middleware(HostFilterMiddleware,
                   **get_host_filter_middleware_settings().model_dump())
