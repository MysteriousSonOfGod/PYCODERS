import psycopg2
import os
cmd="python wikipedia.py"
class SaveDataInPsql:


    def __init__(self):
        self.conn=psycopg2.connect(database="postgres", user="postgres", password="Ravi@143", host='127.0.0.1', port='5432')
        self.cur=self.conn.cursor()


    def CreateTable(self):
        try:
            createTable="CREATE TABLE IF NOT EXISTS ENGLISHTOTELUGU (English VARCHAR(50), Telugu VARCHAR(50))"
            self.cur.execute(createTable)
            self.conn.commit()
            return "TABLE IS CREATED"
        except psycopg2.OperationalError:
            return "password authentication failed for user postgres"


    def Store(self, data):
        it = iter(data)
        t = list(zip(it, it))
        self.cur.executemany("INSERT INTO ENGLISHTOTELUGU VALUES(%s, %s)", t)
        self.conn.commit()
        return "Inserted"

    def Counts(self):
        s="SELECT * FROM ENGLISHTOTELUGU"
        r = self.cur.execute(s)
        row = self.cur.fetchall()
        return row

    def fetchData(self):
        try:
            r="SELECT * FROM ENGLISHTOTELUGU"
            self.cur.execute(r)
            r=self.cur.fetchall()
            return r
        except psycopg2.ProgrammingError:
            return "Table Not found in the database"

    def Delete(self):
        self.cur.execute("DROP TABLE ENGLISHTOTELUGU")
        self.CreateTable()
        self.conn.commit()


l=['devastated', 'నాశనం', 'weird', 'అసహజ', 'embrace', 'ఆలింగనం']
f=SaveDataInPsql()
f.CreateTable()
f.Store(l)

