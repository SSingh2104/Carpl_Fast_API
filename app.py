from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import delete

from sqlalchemy.orm import Session

import crud, model, schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app =FastAPI(
    title="Carpl Database",
    description="Carpl Employees Database Operations Through APIs",
    version= "0.1"
)

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/retrieve_all_details_carpl', response_model=List[schema.Carpl])
def retrieve_all_details_carpl(skip : int=0, limit : int=100, db : Session = Depends(get_db)):
    carpl_employee= crud.get_carpl(db=db,skip=skip, limit=limit)
    return carpl_employee

@app.post('/add_new_carpl', response_model=schema.CarplAdd)
def add_new_carpl(capl: schema.CarplAdd, db: Session = Depends(get_db)):
    e_code = crud.get_carpl_by_e_code(db=db, e_code=capl.e_code)
    if e_code:
        raise HTTPException(status_code=400, detail = f"Employee_Code {capl.e_code} already exist in database: {e_code}")
    return crud.add_carpl_to_db(db=db, capl=capl)

@app.delete('/delete_carpl_by_id')
def delete_carpl_by_id(sl_id:int, db: Session= Depends(get_db)):
    details = crud.get_carpl_by_id(db=db,sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No Record Found")
    try:
        crud.delete_carpl_details_by_id(sl_id=sl_id, db =db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete:{e}")
    return {"delete_status":"Success"}

@app.put('/update_carpl_details')
def update_carpl_details(sl_id:int, update_param: schema.UpdateCarpl, db: Session= Depends(get_db)):
    details = crud.get_carpl_by_id(db=db,sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail = f"No Details Found")
    return crud.update_carpl_details(db=db, details = update_param, sl_id=sl_id)