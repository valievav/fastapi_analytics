from typing import Optional

from sqlmodel import SQLModel, Field


class EventModel(SQLModel, table=True):
    __tablename__ = 'events'
    id: Optional[int] = Field(default=None, primary_key=True)  # to autoincrement id
    path: Optional[str] = None
    description: Optional[str] = None
