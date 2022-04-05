from secrets import choice
from turtle import title
import streamlit as st
from database import Movie,Product,engine
from sqlalchemy.orm import sesionmaker

def opendb():
    Sesion = sesionmaker(bind=engine)
    return Sesion


st.title('db')
st.sidebar('db')
oplist = ['add student','view student']
choice = st.selectbox('select  an option',oplist)
if choice == oplist[0]:
    st.heading ('Add a student in detail')
    f = st.form('add movie')
    title = f.text_input('student name')
    year = f.selectbox("title",'[2010,2011,2012,2013,2014]')
    btn = f.form_submit_button('save movie')
    if btn and title and year:
        save(title,year)
        st.sucess('form saved')
elif choice == oplist[1]:
    st.header('view a student detail')
    db = opendb()
    movies = db.query(Movies).all()
    for std in students:
        st.markdown(f'''
           **movie id**:{movie id}
           **title**:{title}
           **year**:{year}''')