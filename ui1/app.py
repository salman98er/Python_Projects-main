from database import Question
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, flash, redirect, render_template, request
app = Flask(__name__)
app.secret_key = "thisisasecretkey"


def opendb():
    engine= create_engine("sqlite:///Database.sqlite")
    Sesion = sessionmaker(bind=engine)
    return Sesion()
@app.route('/', methods=['GET','POST']) 
def index():
    if request.method == "POST":
        question = request.form.get('question')
        op1 = request.form.get('op1')
        op2 = request.form.get('op2')
        op3 = request.form.get('op3')       
        op4= request.form.get('op4')
        ans = request.form.get('ans')
        category= request.form.get('category')
        print(request.form)
        if not question or len(question)<10:
            flash("Question is required and should be atleast 10 characters long","danger")
            return redirect('/') #reloads the page
        elif not op1:
            flash('option 1 is required','danger')
            return redirect('/')
        elif not op2:
            flash('option 1 is required','danger')
            return redirect('/')
        elif not op3:
            flash('option 1 is required','danger')
            return redirect('/')
        elif not op4:
            flash('option 1 is required','danger')
            return redirect('/')
        else:
            db = opendb()
            q = Question(title=question,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans,category=category)
            db.add(q)
            db.commit()
            db.close()
            flash('question added sucessfully')
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contanct')
def contanct():
    return render_template('contanct.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 