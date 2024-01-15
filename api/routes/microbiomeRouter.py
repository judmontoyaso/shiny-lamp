from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..db.queries import query_microbiome

router = APIRouter()

@router.get("/api/microbiome")
async def get_microbiome_data():
    data = query_microbiome()
    return JSONResponse(content={"data": data})
