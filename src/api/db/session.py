import sqlmodel
from sqlmodel import SQLModel, Session

from .db_config import DATABASE_URL
# (!) import models, so they are registered in SQLModel.metadata and init_db creates tables
from api.events.models import EventModel

if DATABASE_URL == '':
    raise NotImplementedError('DATABASE_URL needs to be set')

engine = sqlmodel.create_engine(DATABASE_URL)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
