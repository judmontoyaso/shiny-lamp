from fastapi import APIRouter, FastAPI, Depends, Security, Response
from fastapi.responses import JSONResponse
import json
from ..db.queries import get_microbiome_all, get_taxonomy_all, get_microbiome_by_runid, get_featureCountExtendedView_all, get_featureCountExtendedView_by_project_id
from ..auth0_utils import VerifyToken
from ..redis_connection import get_redis

router = APIRouter() 
auth = VerifyToken()
@router.get("/api/microbiome")
async def get_microbiome_data(response: Response, auth_result: str = Depends(auth.verify), redis=Depends(get_redis)):
    cache_key = "microbiome_data"

    # Intenta obtener la respuesta del caché
    cached_data = await redis.get(cache_key)
    if cached_data:
        print("caching")
        return json.loads(cached_data)

    # Si no está en caché, procesa la solicitud normalmente
    print("nocaching")
    data = get_microbiome_all()

    # Guarda la respuesta en el caché para futuras solicitudes
    await redis.set(cache_key, json.dumps(data), expire=60*60)  # Expira en 1 hora
    return JSONResponse(content={"data": data})

@router.get("/api/taxonomy")
async def get_taxonomy_data(auth_result: str = Security(auth.verify)):
    data = get_taxonomy_all()
    return JSONResponse(content={"data": data})

@router.get("/api/microbiome/{run_id}")
async def read_microbiome(run_id: str, limit: int = 100, auth_result: str = Security(auth.verify)):
        data = get_microbiome_by_runid(run_id, limit)
        return data
 
@router.get("/api/featurecount")
async def get_featurecount_data(auth_result: str = Security(auth.verify)):
    data = get_featureCountExtendedView_all()
    return JSONResponse(content={"data": data})

@router.get("/api/featurecount/{project_id}")
async def read_microbiome(project_id: str, limit: int = 100,auth_result: str = Security(auth.verify)):
        data = get_featureCountExtendedView_by_project_id(project_id, limit)
        return data
