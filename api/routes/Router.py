from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from ..db.queries import get_microbiome_all, get_taxonomy_all, get_microbiome_by_runid

router = APIRouter() 

@router.get("/api/microbiome")
async def get_microbiome_data():
    data = get_microbiome_all()
    return JSONResponse(content={"data": data})

@router.get("/api/taxonomy")
async def get_taxonomy_data():
    data = get_taxonomy_all()
    return JSONResponse(content={"data": data})

@router.get("/api/microbiome/{run_id}")
async def read_microbiome(run_id: str, limit: int = 100):
        data = get_microbiome_by_runid(run_id, limit)
        return data
 
 
 