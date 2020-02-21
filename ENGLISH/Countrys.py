import sqlite3
import os
command="python Countrys.py"
class Country:
    def __init__(self):
        self.conn = sqlite3.connect("wikidata.db")
        self.cursor = self.conn.cursor()
        self.cn = []
        self.cp = []
        self.cc = []
        self.cl = []

    def SaveData(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS CountryNames(CountryName VARCHAR(20), Capital VARCHAR(20), Currency VARCHAR(20), Language VARCHAR(20))")
        return "Successfully Created"

    def ex(self, pu):
        self.cursor.executemany("INSERT INTO CountryNames VALUES (?,?,?,?)", pu)
        self.conn.commit()

    def count(self):
        c="SELECT COUNT(*) FROM CountryNames"
        r=self.cursor.execute(c)
        row=self.cursor.fetchall()
        return row

    def Delete(self):
        cmd="DROP TABLE CountryNames"
        self.cursor.execute(cmd)


purchases = [('Afghanistan', 'Kabul', 'Afghani', 'Pashto'),
             ('Albania', 'Tirane', 'Lek', 'Albanian'),
            ('Argentina','Buenos Aries', 'Argentine Peso','Spanish'),
    ('Australia', 'Canberra','Australia Dollar','English'),
    ('Austria','Vienna','Euro','German'),
    ('Bangladesh','Dhaka','Taka','Bengali'),
    ('Belgium','Brussels','Euro','Dutch French German'),
    ('Bhutan','Thimphu','Bhutanese','Dzongkha'),
    ('Bolivia','Sucre','Boliviano','Spanish'),
    ('Brazil','Brasilia','Real','Portuguese'),
    ('Cambodia','Phnom Penh','Riel','Khmer'),
    ('Cameroon','Yaounde','Central Africal','French English'),
            ]

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