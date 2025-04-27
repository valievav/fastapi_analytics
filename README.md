### This repo contains analytics API

What's used in this project:
1. **FastAPI** - API framework - app location http://127.0.0.1:8002, documentation http://127.0.0.1:8002/docs
2. **Docker & Docker Compose** - for app containerization

**Docker**
1. To build image with docker `docker build -t analytics-api -f Dockerfile .` -> run project `docker run analytics-api` (builds and runs single image)
2. Better approach - **use Docker Compose** - commands from point 1 are moved to docker compose file (with additional setup), need to run **`docker compose up`** or **`docker compose up --watch`** (to have images rebuilt based on updated docker files or requirements) -> `docker compose down`


**To run project `docker compose up` or `docker compose up --watch`**