from pydantic import BaseModel


class PositionAvg(BaseModel):
    country: str
    avg_position: int