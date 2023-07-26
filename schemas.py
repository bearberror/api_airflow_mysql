from pydantic import BaseModel
from datetime import date, time

class PMResponse(BaseModel):

    transaction_id: str
    station_id: str
    station_name: str
    station_type: str
    lat: float
    long: float
    date: date
    time: time
    pm25: float | None = None
    pm10: float | None = None
    o3: float | None = None
    no2: float | None = None
    so2: float | None = None
    province: str
    district: str | None = None
    subdistrict: str | None = None

    class Config:
        from_attributes = True

class OdpcResponse(BaseModel):
    odpc: int
    provinces_list: str

class PMInsert(BaseModel):

    transaction_id: str
    station_id: str
    station_name: str
    station_type: str
    lat: float
    long: float
    date: date
    time: time
    pm25: float | None = None
    pm10: float | None = None
    o3: float | None = None
    no2: float | None = None
    so2: float | None = None
    province: str
    district: str | None = None
    subdistrict: str | None = None