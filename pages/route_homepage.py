from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/stats.html")
async def home(request: Request):
    return templates.TemplateResponse("/stats.html", {"request": request})
