from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.config import MONGODB_URL
from app.database.mongodb import get_database

from app.api.api import api


def overwrite_connection():
    try:
        client_test = AsyncIOMotorClient(str(MONGODB_URL))
        yield client_test
    finally:
        client_test.close()


api.dependency_overrides_provider[get_database] = overwrite_connection
client = TestClient(api)


def test_ip():
    response = client.get("/ip/8.8.8.8", headers={"user-id": "david"})
    assert response.status_code == 200
    assert response.json() == {
        "ip": "8.8.8.8",
        "fecha_actual": "27/09/2021 22:02:11 GMT",
        "pais": "united states",
        "iso_code": "us",
        "distancia_estimada": "9328 km",
        "pertenece_a_aws": False
    }
