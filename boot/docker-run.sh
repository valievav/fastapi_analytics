#!/bin/bash

# contains PROD setup to run gunicorn server with multiple workers (for better performance, fault tolerance etc.)

source /opt/venv/bin/activate

cd /code
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app