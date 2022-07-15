import profile
from sqlalchemy.orm import Session
from schema import Carpl
import model
import schema


def get_carpl_by_e_code(db: Session, e_code: str):
    return db.query(model.CARPL).filter(model.CARPL.e_code == e_code).first()

def get_carpl_by_id(db: Session, sl_id: int):
    return db.query(model.CARPL).filter(model.CARPL.id == sl_id).first()

def get_carpl(db:Session, skip: int =0, limit:int=100):
    return db.query(model.CARPL).offset(skip).limit(limit).all()

def add_carpl_to_db(db: Session, capl: schema.CarplAdd):
    carp_details = model.CARPL(
        e_code = capl.e_code,
        e_name = capl.e_name,
        designation = capl.designation,
        dob = capl.dob,
        active = capl.active,
        email = capl.email,
        profile = capl.profile

    )
    db.add(carp_details)
    db.commit()
    db.refresh(carp_details)
    return model.CARPL(**capl.dict()) #It will return dictionary object of record which inserted.

def update_carpl_details(db: Session, sl_id: int, details: schema.UpdateCarpl):
    db.query(model.CARPL).filter(model.CARPL.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.CARPL).filter(model.CARPL.id == sl_id).first()

def delete_carpl_details_by_id(db: Session, sl_id:int):
    try:
        db.query(model.CARPL).filter(model.CARPL.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)