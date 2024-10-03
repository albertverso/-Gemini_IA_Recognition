from app.models import Vehicle
from app import db

def add_vehicle(license_plate, model, color, year, owner):
    new_vehicle = Vehicle(license_plate=license_plate, model=model, color=color, year=year, owner=owner)
    db.session.add(new_vehicle)
    db.session.commit()

def search_vehicle_by_plate(license_plate):
    return Vehicle.query.filter_by(license_plate=license_plate).first()
