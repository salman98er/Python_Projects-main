from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/',methods = ["GET","POST"])
def index():
    if request.method == "POST":
        return render_template('index.html')
    return render_template('index.html')
    
@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/help')
def help():
    return render_template('help.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)