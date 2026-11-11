from fastapi import FastAPI
from httpx import AsyncClient, HTTPError
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.logging import logger
from app.core import http


@asynccontextmanager
async def lifespan(app: FastAPI):
    target = f"{settings.BOT_WEBHOOK_URL}/webhook"

    # Initialize HTTP client
    http.http_client = AsyncClient(timeout=10.0)
    try:
        # Register Telegram webhook
        res = await http.http_client.post(
            f"{settings.TELEGRAM_BOT_API}/setWebhook",
            json={
                "url": target,
                "secret_token": settings.BOT_WEBHOOK_SECRET
            }
        )

        res.raise_for_status()

        data = res.json()
        if not data.get("ok"):
            raise RuntimeError(
                f"Telegram webhook registration failed: {data}"
            )
        logger.info("Telegram webhook registered: %s", target)

        yield
    except (HTTPError, RuntimeError):
        logger.exception("FastAPI lifespan operation failed.")
        raise
    finally:
        # Close HTTP client during shutdown
        if http.http_client is not None:
            await http.http_client.aclose()
            http.http_client = None
        logger.info("FastAPI application shutting down.")