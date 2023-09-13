from fastapi import FastAPI, APIRouter , status
from app import models,user
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .user import router as person_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

router = APIRouter()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(person_router,tags=["Person"], prefix="/api") 






