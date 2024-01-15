from fastapi import FastAPI
from .routes.microbiomeRouter import router as microbiome_router
from .routes.taxonomyRouter import router as taxonomy_router

app = FastAPI()

app.include_router(microbiome_router)
app.include_router(taxonomy_router)
