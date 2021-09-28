from pydantic import BaseModel, Field


class IpResponse(BaseModel):
    ip: str = Field(...)
    fecha_actual: str = Field(...)
    pais: str = Field(...)
    iso_code: str = Field(...)
    distancia_estimada: str = Field(...)
    pertenece_a_aws: bool = False


class IpHomeCheck(BaseModel):
    status: int
