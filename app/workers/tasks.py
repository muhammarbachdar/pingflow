from app.workers.celery_app import celery_app
from app.models.notification import Notification, NotificationStatus, NotificationLog
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

def get_sync_session():
    engine = create_async_engine(settings.DATABASE_URL)
    return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def _process(notification_id: int):
    SessionLocal = get_sync_session()
    async with SessionLocal() as db:
        result = await db.execute(
            select(Notification).where(Notification.id == notification_id)
        )
        notification = result.scalar_one_or_none()
        if not notification:
            return

        try:
            print(f"Sending via {notification.channel} to {notification.recipient}")
            notification.status = NotificationStatus.SENT
            log = NotificationLog(
                notification_id=notification_id,
                status="sent",
                message="Delivered successfully"
            )
            db.add(log)
            await db.commit()
        except Exception as e:
            notification.status = NotificationStatus.FAILED
            log = NotificationLog(
                notification_id=notification_id,
                status="failed",
                message=str(e)
            )
            db.add(log)
            await db.commit()

@celery_app.task(bind=True, max_retries=3)
def send_notification(self, notification_id: int):
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(_process(notification_id))
    finally:
        loop.close()
    return {"status": "processed", "id": notification_id}