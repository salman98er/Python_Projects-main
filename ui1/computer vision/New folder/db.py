from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float ,DateTime
from datetime import datetime 

import streamlit as st
from data import Movies
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def opendb():
    engine= create_engine("sqlite:///movies.sqlite")
    Sesion = sessionmaker(bind=engine)
    return Sesion()
def save_movie(title,year):
    db = opendb()
    movie =Movies(title = title,year = year)
    db.add(movie)
    db.commit()
    db.close()
st.title(Movies)
