from fastapi import FastAPI
from app.db import engine
from app import models
from app.egg_routes import router as egg_router
from dotenv import load_dotenv

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(egg_router, prefix="/api/v1", tags=["eggs"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
