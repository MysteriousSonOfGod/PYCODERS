import sqlite3

class Wikipi:
    def __init__(self):
        self.conn=sqlite3.connect("/home/ravi/Documents/PYCODERS/ENGLISH/wikidata.db")
        self.cursor=self.conn.cursor()

    def collect(self):
        cmd="SELECT * FROM ENGLISH"
        self.cursor.execute(cmd)
        data=self.cursor.fetchall()
        return data

