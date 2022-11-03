from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend import templates

import os

from pathlib import Path

general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})

