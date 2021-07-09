# an object for WSGI application
from flask import Flask,redirect,url_for
from flask import *
from werkzeug.utils import find_modules
app = Flask(__name__)

# which url i want to access
@app.route('/')
def home(): 
    return render_template('index.html') 

@app.route('/courses')
def courses():
    return "<h1>Flask baisc tutorial</h1>"

@app.route('/<name>')  #dynamic content
def user(name):
    return f"<h1>Hello {name}! Welcome to the future!!<h1>"   

@app.route('/submit',methods=['POST','GET'])
def submit():
    marks = 0
    if request.method =='POST':
        phy = float(request.form['Physics'])
        ch = float(request.form['Chemistry'])
        math = float(request.form['Math'])
        tot = (phy+ch+math)/3 
    res=tot
    return redirect(url_for('success',marks=res))


@app.route('/results/<int:marks>')
def results(marks):
    return redirect(url_for('success',marks=marks))

@app.route('/success/<int:marks>')
def success(marks):
    final = ""
    if marks<45:
        final = "fail"
    else:
        final = "pass"
    exp={'Number':marks,'Result':final}
    return render_template('result.html',result=exp)

@app.route('/about')
def about():
    return render_template('about.html')
        
if __name__=='__main__':
    app.run(debug=True)