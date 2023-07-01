from fastapi import FastAPI

app = FastAPI()

from domain.result import result_router
from domain.model import names_router

app.include_router(result_router.router)
app.include_router(names_router.router)