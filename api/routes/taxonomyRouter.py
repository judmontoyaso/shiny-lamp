from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..db.queries import query_taxonomy

router = APIRouter()

@router.get("/api/taxonomy")
async def get_data():
    data = query_taxonomy()
    return JSONResponse(content={"data": data})

