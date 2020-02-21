#REFERENCE https://docs.python.org/3/library/sqlite3.html
import sqlite3
import os
class Wikipedia:
    def __init__(self):
        self.el = []
        self.le = []
        self.conn=sqlite3.connect("wikidata.db")
        self.cursor=self.conn.cursor()
    def EnglishWords(self, l):
        for i in range(0, len(l)):
            if i % 2 == 0:
                self.el.append(l[i])
        for j in range(0, len(l)):
            if j % 2 != 0:
                self.le.append(l[j])
        it=iter(self.el)
        it1=iter(self.le)
        self.res=dict(zip(it, it1))
        return self.res

    def SaveData(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS GRAMMAR(Name VARCHAR(200), Telugu VARCHAR(200))")
        self.SaveDetails()
        return "Successfully Created"

    def Count(self):
        r="SELECT COUNT(*) FROM GRAMMAR"
        k=self.cursor.execute(r)
        row=self.cursor.fetchall()
        return row

    def SaveDetails(self):
        for i, j in self.res.items():
            self.cursor.execute("INSERT INTO GRAMMAR (Name, Telugu) VALUES(?, ?)", (i, j))
            self.conn.commit()

    def Detele(self):
        cmd="DROP TABLE GRAMMAR"
        self.cursor.execute(cmd)
        self.SaveData()
        return "Yes"

l = []

e=[]
r=Wikipedia()
s=r.EnglishWords(l)
if bool(s):
    r.SaveData()
else:
    print(s)

f=r.Count()
for i in f:
    for j in i:
        if j==0:
            r.SaveDetails()
        elif j==len(l):
            print("DATA STORES")
        else:
            r.Detele()