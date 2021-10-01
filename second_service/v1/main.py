from typing import Optional

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
)
from fastapi.staticfiles import StaticFiles
import subprocess

app = FastAPI(
        title="SoA-Second",
        description="SoA-Second: Documentation",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        root_path="/api/v1/second-service"
        )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="/app/app/static"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/api/v1/second-service/openapi.json",
        title=app.title,
        swagger_favicon_url="/static/logo.png",
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url="/api/v1/second-service/openapi.json",
        title=app.title + " - ReDoc",
        redoc_favicon_url="/static/logo.png",
    )

@app.get("/", include_in_schema=False)
async def root():
    response = RedirectResponse(url='/api/v1/second-service/docs')
    return response

@app.get("/system")
async def root():
    try:
        process  = subprocess.run(["uname",'-a'],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'success', 'data': process.stdout} 
    except Exception as e:
        return {"status":"failed", "message": str(e)}