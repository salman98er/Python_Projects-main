import streamlit as st
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float ,DateTime
from datetime import datetime 
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Movies(Base):
    __tablename__="movies"
    id = Column(Integer,primary_key=True)
    title =Column(String(50))
    year = Column(Integer)
    director =  Column(String(25))
    genre = Column(String)
    rating = Column(Integer)
    summary =Column(String)
    release_date = Column(DateTime,default = datetime.now)
    added = Column(DateTime,default = datetime.now)
 
engine = create_engine("sqlite:///movies.sqlite",echo = True)
Base.metadata.create_all(engine)