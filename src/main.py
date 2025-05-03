from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.db.session import init_db
from api.events.routing import router as event_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f'Server is starting...')
    init_db()
    yield
    print(f'Server has been stopped')


app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix='/api/events')


@app.get('/')
async def root():
    return {'message': 'Hello World! It"s me - VV :)!'}


@app.get('/healthz')
async def get_api_health():
    return {'status': 'ok'}
