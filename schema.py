import profile
from typing import Optional
from pydantic import BaseModel

class CarplBase(BaseModel):
    e_name:str
    designation:str
    dob:str
    email:str

class CarplAdd(CarplBase):
    e_code:str
    profile: Optional[str] =None
    active: bool

    class Config:
        orm_mode = True

class Carpl(CarplAdd):
    id: int

    class Config:
        orm_mode = True

class UpdateCarpl(BaseModel):
    profile: Optional[str] = None
    active: bool

    class Config:
        orm_mode = True