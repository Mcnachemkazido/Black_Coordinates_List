from pydantic import BaseModel


class Location(BaseModel):
    query: str
    lat: float
    lon: float

