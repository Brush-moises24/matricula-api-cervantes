from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter(
    tags=["Páginas"]
)


CARPETA_FRONTEND = Path(__file__).resolve().parent.parent.parent / "frontend"


@router.get("/", include_in_schema=False)
def pagina_inicio():
    return FileResponse(CARPETA_FRONTEND / "index.html")