import logging
from motor.motor_asyncio import AsyncIOMotorClient
from ..config.config import MONGODB_URL
from ..database.mongodb import db


async def connect_mongodb():
    logging.info("Connecting to database")
    db.client = AsyncIOMotorClient(str(MONGODB_URL), maxPoolSize=100)
    logging.info("Connection established")


async def close_mongodb_connection():
    db.client.close()
    logging.info("Close connection")
