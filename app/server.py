# The Book Store API
from . import __title__, __version__, __description__, __feature__
# from app.database import SessionLocal
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
import logging
import os


api = FastAPI(
    title=__title__,
    description=__description__,
    version=__version__,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@api.get("/", tags=["system"])
def get_info():
    """
    Returns name, version and description
    """
    return {
        "title": __title__,
        "description": __description__,
        "version": __version__,
        "feature": __feature__,
        "commit": os.getenv("COMMIT_SHA"),
        "timestamp": os.getenv("TIMESTAMP"),
    }
