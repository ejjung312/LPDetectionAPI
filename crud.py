from sqlalchemy.orm import Session
import models, schemas

def get_license_plate(db: Session, text: str):
    return db.query(models.LicensePlate).filter(models.LicensePlate.vehicle_number == text).first()

# def create_license_plate(db: Session, lp: schemas.LPCreate):
def create_license_plate(db: Session, lp: str):
    db_lp = models.LicensePlate(vehicle_number=lp)
    db.add(db_lp)
    db.commit()
    db.refresh(db_lp)

    return db_lp