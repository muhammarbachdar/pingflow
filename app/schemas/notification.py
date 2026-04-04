from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class ChannelEnum(str, Enum):
    EMAIL = "email"
    WEBHOOK = "webhook"

class NotificationCreate(BaseModel):
    channel: ChannelEnum
    recipient: str
    subject: str
    body: str

class NotificationResponse(BaseModel):
    id: int
    channel: ChannelEnum
    recipient: str
    subject: str
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}