from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, DateTime

def get_utc_now():
    return datetime.now(timezone.utc)


class EventModel(SQLModel, table=True):
    __tablename__ = 'events'
    id: Optional[int] = Field(default=None, primary_key=True)  # autoincrement id (can be None so db can generate id)
    path: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=get_utc_now,
                                 sa_type=DateTime(timezone=True),
                                 nullable=False)
    updated_at: datetime = Field(default_factory=get_utc_now,
                                 sa_type=DateTime(timezone=True),
                                 nullable=False)
