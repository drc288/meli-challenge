from pydantic import BaseModel


class BaseIp(BaseModel):
    user_id: str
    ip: str

class