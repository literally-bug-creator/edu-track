from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import AuthRouter
from .unit import UnitRouter
from .track import TrackRouter
from .discipline import DisciplineRouter
from .group import GroupRouter

app = FastAPI(title="EduTrack API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(AuthRouter)
app.include_router(UnitRouter)
app.include_router(TrackRouter)
app.include_router(DisciplineRouter)
app.include_router(GroupRouter)
