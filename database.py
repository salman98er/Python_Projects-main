from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float ,DateTime
from datetime import datetime 

Base = declarative_base()

class Movie(Base):
    __tablename__="movies"
    id = Column(Integer,primary_key=True)
    title =Column(String(50))
    year = Column(Integer)
    director =  Column(String(25))
    genre = Column(String)
    rating = Column(Integer)
    summary =Column(String)

class Product(Base):
 __tablename__ = 'products'
 id = Column(Integer,primary_key=True)
 title = Column(String,unique = True) 
 mrp = Column(Float , default = 0.0)
 quantity = Column(Integer,default = 0) 
 brand = Column(String(50),default="no brand")
 detail = Column(String,default = ' ')
 mfg = Column(DateTime,default = datetime.now)
 added_on = Column(DateTime,default = datetime.now)
 
engine = create_engine("sqlite:///school.sqlite",echo = True)
Base.metadata.create_all(engine)