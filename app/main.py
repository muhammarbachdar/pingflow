from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.auth import router as auth_router
from app.api.routes.notifications import router as notifications_router



app = FastAPI(
    title="PingFlow",
    description="Multi-channel notification engine",
    version="0.1.0"
)

app.include_router(auth_router)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "PingFlow"}

app.include_router(notifications_router)