from fastapi import APIRouter, FastAPI, Depends, Security
from fastapi.responses import JSONResponse
from ..db.queries import get_microbiome_all, get_taxonomy_all, get_microbiome_by_runid, get_featureCountExtendedView_all, get_featureCountExtendedView_by_project_id
from ..auth0_utils import VerifyToken

router = APIRouter() 
auth = VerifyToken()

@router.get("/api/microbiome")
async def get_microbiome_data(auth_result: str = Security(auth.verify)):
    data = get_microbiome_all()
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
