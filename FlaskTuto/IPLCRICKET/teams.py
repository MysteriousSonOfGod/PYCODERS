import sqlite3

class DATA:
    def __init__(self):
        self.conn = sqlite3.connect("/home/ravi/Documents/PYCODERS/SQLite3/IPL.db")
        self.cur = self.conn.cursor()

    def DisplaySchedule(self):
        r=self.cur.execute("SELECT team, date FROM IPLSCHEDULE")
        d=self.cur.fetchall()
        e=[]
        for r in d:
            for i in r:
                e.append(i)
        di = iter(e)
        dic = dict(zip(di, di))
        return dic
