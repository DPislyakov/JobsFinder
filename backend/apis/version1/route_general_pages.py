from fastapi import APIRouter
from fastapi import Request

from backend import templates

general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request}
    )
