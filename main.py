from fastapi import FastAPI

import py_eureka_client.eureka_client as eureka_client
import py_eureka_client.logger as logger

from domain.result import result_router
from domain.model import names_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
	await eureka_client.init_async(eureka_server="http://127.0.0.1:8761/eureka",
                                   app_name="AI-MODEL-SERVER",
                                   instance_port=8000)

app.include_router(result_router.router)
app.include_router(names_router.router)