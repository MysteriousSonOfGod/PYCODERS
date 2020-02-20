import psycopg2
from flask import Flask, render_template, request, redirect
app=Flask(__name__)
from ravi import *

@app.route("/")
def home():
    return render_template("ipl.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/savedetails", methods=["POST"])
def savedetails():
    if request.method=='POST':
        name=request.form["name"]
        psd=request.form["psd"]
        repass=request.form["repass"]
        go=ATI()
        if psd==repass:
            return go.registerTeam(name, psd)
        return render_template("ipl.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/disp", methods=["POST"])
def disp():
    if request.method=='POST':
        name=request.form["name"]
        passw=request.form["passw"]
        go=ATI()
        return go.validate(passw, name)




# @app.route("/vi", methods=["POST"])
# def vi():
#     if request.method=='POST':
#         name = request.form["name"]
#         ps = request.form["ps"]
#         conn = psycopg2.connect(database="postgres", user='postgres', password='Ravi@143', host='127.0.0.1',
#                                 port='5432')
#         cursor = conn.cursor()
#         record = """SELECT * FROM allteams"""
#         row=cursor.execute(record)
#         # import pdb
#         # pdb.set_trace()

if __name__=="__main__":
    app.run(debug=True)














# from flask import *
#
# app = Flask(__name__)
# app.secret_key = "ayush"
#
#
# @app.route('/')
# def home():
#     return render_template("home.html")
#
#
# @app.route('/login')
# def login():
#     return render_template("login.html")
#
#
# @app.route('/success', methods=["POST"])
# def success():
#     if request.method == "POST":
#         session['email'] = request.form['email']
#     return render_template('success.html')
#
#
# @app.route('/logout')
# def logout():
#     if 'email' in session:
#         session.pop('email', None)
#         return render_template('logout.html');
#     else:
#         return '<p>user already logged out</p>'
#
#
# @app.route('/profile')
# def profile():
#     if 'email' in session:
#         email = session['email']
#         return render_template('profile.html', name=email)
#     else:
#         return '<p>Please login first</p>'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
