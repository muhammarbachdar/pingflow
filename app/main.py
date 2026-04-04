from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes.auth import router as auth_router
from app.api.routes.notifications import router as notifications_router

app = FastAPI(
    title="PingFlow",
    description="Multi-channel notification engine",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(notifications_router)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "PingFlow"}