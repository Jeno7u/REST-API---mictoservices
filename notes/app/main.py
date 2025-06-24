from fastapi import FastAPI
from app.api.v1.notes import router as notes_router

app = FastAPI()
app.include_router(notes_router, prefix="/notes", tags=["Notes"])
