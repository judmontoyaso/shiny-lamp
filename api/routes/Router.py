from fastapi import APIRouter, FastAPI, Depends, Security, Response
from fastapi.responses import JSONResponse
import json
from ..db.queries import get_microbiome_all, get_taxonomy_all, get_microbiome_by_runid, get_featureCountExtendedView_all, get_featureCountExtendedView_by_project_id
from ..auth0_utils import VerifyToken
from ..redis_connection import get_redis


router = APIRouter() 
auth = VerifyToken()
@router.get("/api/microbiome")
async def get_microbiome_data(response: Response, auth_result: str = Security(auth.verify), redis=Depends(get_redis)):
    data = await caching_data("microbiome_data", get_microbiome_all, redis)
    return data

@router.get("/api/taxonomy")
async def get_taxonomy_data(auth_result: str = Security(auth.verify), redis=Depends(get_redis)):
    data = await caching_data("taxonomy_data", get_taxonomy_all, redis)
    return data

@router.get("/api/microbiome/{run_id}")
async def read_microbiome(run_id: str, limit: int = 100, auth_result: str = Security(auth.verify), redis=Depends(get_redis)):
        cache_key = "_".join(["microbiome_data", run_id])
        data = await caching_data(cache_key , get_microbiome_by_runid, redis, run_id, limit)
        return data
 
@router.get("/api/featurecount")
async def get_featurecount_data(response: Response, auth_result: str = Security(auth.verify), redis=Depends(get_redis)):
    data = await caching_data("featurecount" , get_featureCountExtendedView_all, redis)
    return data

@router.get("/api/featurecount/{project_id}")
async def read_microbiome(project_id: str, limit: int = 100,auth_result: str = Security(auth.verify), redis=Depends(get_redis)):
        cache_key = "_".join(["featurecount", project_id])
        data = await caching_data(cache_key , get_featureCountExtendedView_by_project_id, redis, project_id, limit)
        return data


async def caching_data(cache_key, data_function, redis, *args, **kwargs):
    # Intenta obtener la respuesta del caché
    cached_data = await redis.get(cache_key)
    if cached_data:
        print("caching")
        return JSONResponse(content={"data": json.loads(cached_data)})

    # Si no está en caché, procesa la solicitud normalmente
    print("nocaching")
    data = data_function(*args, **kwargs)  # Pasando argumentos a la función
    # Guarda la respuesta en el caché para futuras solicitudes
    await redis.set(cache_key, json.dumps(data), ex=60*60)  # Expira en 1 hora
    return JSONResponse(content={"data": data})

