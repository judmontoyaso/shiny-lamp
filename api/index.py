from fastapi import FastAPI
from .routes.Router import router

app = FastAPI()

app.include_router(router)
