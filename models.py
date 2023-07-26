from sqlalchemy import Column, Integer, String, Float, Date, Time
from database import Base
from datetime import date, time

## Setup data models

class PMData(Base):
    __tablename__ = "pm"

    transaction_id = Column(String(100), primary_key= True)
    station_id = Column(String(100))
    station_name = Column(String(100))
    station_type = Column(String(20))
    lat = Column(Float)
    long = Column(Float)
    date = Column(Date)
    time = Column(Time)
    pm25 = Column(Float)
    pm10 = Column(Float)
    o3 = Column(Float)
    no2 = Column(Float)
    so2 = Column(Float)
    province = Column(String(100))
    district = Column(String(100))
    subdistrict = Column(String(100))

class Odpc(Base):
    __tablename__ = "odpc"

    odpc = Column(Integer, primary_key= True)
    provinces_list = Column(String(500))