import psycopg2
from flask import Flask, render_template, request, redirect
app=Flask(__name__)

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
        if psd==repass:
            conn = psycopg2.connect(database="postgres", user='postgres', password='Ravi@143', host='127.0.0.1', port='5432')
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS allteams (name VARCHAR(20), password VARCHAR(20))")
            postgres_insert_query = """ INSERT INTO allteams (name, password) VALUES (%s,%s)"""
            record_to_insert = (name, psd)
            cursor.execute(postgres_insert_query, record_to_insert)
            # cursor.execute("INSERT INTO allteams (name,password) values({}{})".format(name, psd))
            conn.commit()
        return render_template("ipl.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/vi", methods=["POST"])
def vi():
    if request.method=='POST':
        name = request.form["name"]
        ps = request.form["ps"]
        conn = psycopg2.connect(database="postgres", user='postgres', password='Ravi@143', host='127.0.0.1',
                                port='5432')
        cursor = conn.cursor()
        record = """SELECT * FROM allteams"""
        row=cursor.execute(record)
        # import pdb
        # pdb.set_trace()

if __name__=="__main__":
    app.run(debug=True)

