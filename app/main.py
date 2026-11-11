from fastapi import FastAPI
from app.core.config import settings
from app.core.database.dependency import init_db
from app.lifespan import lifespan
from app.interfaces.telegram.webhook import router as tg_router

# Initialise the Database Connection
# init_db()

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

app.include_router(tg_router)

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service_name": f"{settings.PROJECT_NAME} {settings.PROJECT_VERSION}"
    }