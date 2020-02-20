import psycopg2
import onetimepad
from flask import render_template
class ATI:
    def __init__(self):
        self.conn=psycopg2.connect(database="postgres", user='postgres', password='Ravi@143', host='127.0.0.1', port='5432')
        self.cursor=self.conn.cursor()


    # def csktm(self, ID, name, price, city):
    #     self.cursor.execute("CREATE TABLE IF NOT EXISTS cskteam (ID INT PRIMARY KEY NOT NULL, palyername VARCHAR(20) NOT NULL, price REAL, city CHAR(50))")
    #     postgres_insert_query = """ INSERT INTO allteams (ID, palyername,price, city) VALUES (%s,%s,%s,%s)"""
    #     record_to_insert = (ID, name, price, city)
    #     self.cursor.execute(postgres_insert_query, record_to_insert)
    #     self.conn.commit()

    def registerTeam(self, name, ps):
        msg="USER IS CREATED"
        cipherText=onetimepad.encrypt(ps, 'random')
        self.cursor.execute("CREATE TABLE IF NOT EXISTS allteams (UserName VARCHAR(50), Password VARCHAR(20), Cipher VARCHAR(20))")
        postgres_insert_query = """ INSERT INTO allteams (UserName, Password, Cipher) VALUES (%s,%s,%s)"""
        record_to_insert = (name, ps, cipherText)
        self.cursor.execute(postgres_insert_query, record_to_insert)
        self.conn.commit()
        return render_template("success.html", msg=msg)

    def validate(self, passw, name):
        self.cursor.execute("SELECT UserName, Password FROM allteams")
        rows=self.cursor.fetchall()
        for i, j in rows:
            if i=="CSK" and j==passw:
                return render_template("csk.html")
            elif i=="DD" and j==passw:
                return render_template("dd.html")