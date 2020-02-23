import sqlite3
import os
command="python InsertIPL2020.py"
class Country:
    def __init__(self):
        self.conn = sqlite3.connect("rcb.db")
        self.cursor = self.conn.cursor()
        self.cn = []
        self.cp = []
        self.cc = []
        self.cl = []

    def SaveData(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rcbplayers (ID INT, palyername varchar(20), price INT, city VARCHAR(20))")
        return "Successfully Created"

    def ex(self, pu):
        self.cursor.executemany("INSERT INTO rcbplayers (ID, palyername, price, city) VALUES (?,?,?,?)", pu)
        self.conn.commit()

    def count(self):
        c="SELECT COUNT(*) FROM rcbplayers"
        r=self.cursor.execute(c)
        row=self.cursor.fetchall()
        return row

    def Delete(self):
        cmd="DROP TABLE rcbplayers"
        self.cursor.execute(cmd)


purchases = [(18, 'Virat Kohili', 150000000, 'Delhi'),
             (29,'Gurkeerat Singh', 5000000, 'Punjab'),
             (7,'Shivam Dube', 50000000,'Mumbai'),
             (8, 'Moeen Ali', 15000000, 'England')]

re=Country()
r=re.SaveData()
re.ex(purchases)
f=re.count()
for i in f:
    for j in i:
        if j==0:
            re.SaveData()
        elif j==len(purchases):
            print("Added")
        else:
            re.Delete()
            os.system(command)