from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.notes import router as notes_router


app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(notes_router, prefix="/notes", tags=["Notes"])
