from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class LicensePlate(Base):
    __tablename__ = 'license_plate'

    idx = Column(Integer, primary_key=True, index=True)
    vehicle_number = Column(String(32), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True, default=func.now())