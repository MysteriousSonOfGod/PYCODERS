from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html");


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            passw = request.form["psd"]
            repassw = request.form["repass"]
            if passw==repassw:
                with sqlite3.connect("iplteams.db") as con:
                    cur = con.cursor()
                    cur.execute("CREATE TABLE IF NOT EXISTS allteams (name VARCHAR(20), password VARCHAR(20))")
                    cur.execute("INSERT into allteams (name,password) values (?,?)", (name, passw))
                    con.commit()

            else:
                msg = "Password is not matching"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

# @app.route('/login', methods=["POST"])
# def login():
#     if request.method=="POST":
#         try:
#             name=request.form["name"]
#             ps=request.form["ps"]
#             with sqlite3.connect("iplteams.db") as conn:
#                 cur = conn.cursor()
#                 cur.execute("SELECT * FROM allteams")
#                 rows = cur.fetchall()
#                 import pdb
#                 pdb.set_trace()
#                 conn.commit()
#                 msg = "Employee successfully Added"
#         except:
#             conn.rollback()
#             msg = "We can not add the employee to the list"
#
#         finally:
#             return render_template("success.html", msg=msg)
#             conn.close()


@app.route("/view", methods=["POST"])
def view():
    if request.method == "POST":
        try:
            name=request.form["name"]
            ps=request.form["ps"]
            with sqlite3.connect("iplteams.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM allteams")
                rows = cur.fetchall()
                tp=name, ps
                import pdb
                pdb.set_trace()
                for i in range(0, len(rows)):

                    pass
        except:
            conn.rollback()
    # con = sqlite3.connect("employee.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("select * from Employees")
    # rows = cur.fetchall()
    # return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("employee.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Employees where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)