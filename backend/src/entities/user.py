from sqlalchemy import Column, Integer, String, Boolean
from src.database.database import Base

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, index=True, unique=True)
    password_hash = Column(String(255), nullable=False) 
    firstname = Column(String(100))  
    lastname = Column(String(100))   
    age = Column(Integer) 
    contact = Column(String(15), index=True)
    city = Column(String(100), index=True)
    pincode = Column(String(10), index=True)
    state = Column(String(100), index=True)
    house_detail = Column(String(255))
    