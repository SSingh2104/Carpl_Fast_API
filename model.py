import profile
from sqlalchemy import Column, String, Boolean, Integer

from db_handler import Base

class CARPL(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key = True, autoincrement = True, index =True, nullable= False)
    e_code = Column(String, unique =True, index =True, nullable=False)
    e_name = Column(String(255), index =True, nullable=False)
    designation = Column(String(100), index=True, nullable=False)
    dob = Column(String, index =True, nullable = False)
    active = Column(Boolean, nullable= False, default = True)
    email = Column(String, index =True, nullable = False)
    profile = Column(String, index =True)