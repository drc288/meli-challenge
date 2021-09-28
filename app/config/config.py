import os
from dotenv import load_dotenv
from databases import DatabaseURL

load_dotenv(".env")

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DB = os.getenv("MONGO_DB")


MONGODB_URL = DatabaseURL(
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@meli-challenge.oqbde.mongodb.net/{MONGO_DB}?retryWrites=true&w=majority"
)


