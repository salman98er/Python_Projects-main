from secrets import choice
from turtle import title
from numpy import save
import streamlit as st
from database import Movie,Product,engine
from sqlalchemy.orm import sessionmaker

def opendb():
    Sesion = sessionmaker(bind=engine)
    return Sesion


    def save_student(title,year):
        db = opendb()
        movie =Movie(title = title,year = year)
        db.add(movie)
        db.commit()
        db.close()


st.title('db')
st.sidebar.title('db')
oplist = ['add student','view student']
choice = st.selectbox('select  an option',oplist)
if choice == oplist[0]:
    st.header('Add a student in detail')
    f = st.form('add movie')
    title = f.text_input('movie  name')
    year = f.selectbox("title",[1,23,44,55])
    btn = f.form_submit_button('save movie')
    if btn and title and year:
        save(title,year)
        st.success('form saved')
elif choice == oplist[1]:
    st.header('view a student detail')
    db = opendb()
    movies = db.query(Movie).all()
    for movie in movies:
        st.markdown(f'''
           **movie id**:{movie.id}
           **title**:{movie.title}
           **year**:{movie.year}''')