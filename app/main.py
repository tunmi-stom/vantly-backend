from fastapi import FastAPI
from app.core.config import settings
from app.core.database.dependency import init_db

# Initialise the Database Connection
init_db()

app = FastAPI()

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service_name": f"{settings.PROJECT_NAME} {settings.PROJECT_VERSION}"
    }