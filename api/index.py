from fastapi import FastAPI
from .routes.Router import router
from redis import asyncio as aioredis

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.redis = await aioredis.from_url(
    url=f"redis://redis:6379",
    decode_responses=True
)

@app.on_event("shutdown")
async def shutdown():
    app.state.redis.close()
    await app.state.redis.wait_closed()

app.include_router(router)
