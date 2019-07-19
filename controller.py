from flask import Flask,render_template,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///myportal.sqlite3'

db=SQLAlchemy(app)

class Sample(db.Model):
    id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email=db.Column(db.String(50))
    phno=db.Column(db.String(20))


    def __init__(self,name,email,phno):
        self.name=Name
        self.email=email
        self.phno=  phno


@app.route('/mypage/register',methods=['POST','GET'])
def register():
    if request.method== "POST":
        name=request.form['fname']
        email=request.form['emailid']
        mobile=request.form['mobile']
        password=request.form['password']
        # # print(name,email,mobile)
        flash("Registration completed successfully")
        return render_template('display.html',tname=name,temail=email,tmobile=mobile,tpassword=password)
    flash("Register your account")
    return render_template('register.html')

@app.route('/mypage/login')
def login():

    return render_template('login.html')

# @app.route('/mypage/display')
# def display():
    # name="kalyan"
    #return render_template('display.html'name=fname)
    # return "my name is {}".format(name)
if __name__== '__main__':
    app.secret_key="my heart"
    db.create_all()
    app.run(debug=True)
