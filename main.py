from fastapi import FastAPI

app = FastAPI()

from domain.result import result_router

app.include_router(result_router.router)