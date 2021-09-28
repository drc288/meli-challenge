from pydantic import BaseModel


class DistanceResponse(BaseModel):
    ip: str
    pais: str
    distancia: str
    invocaciones: int