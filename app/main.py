from database.mongodbutils import close_mongodb_connection, connect_mongodb
from .api.api import api
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI(title="meli challenge", description="mercado libre challenge", version="0.0.1")

app.add_event_handler("startup", connect_mongodb)
app.add_event_handler("shutdown", close_mongodb_connection)
app.include_router(api)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)