import psycopg2
from main import *
class ATI:
    def __init__(self):
        self.conn=psycopg2.connect(database="postgres", user='postgres', password='Ravi@143', host='127.0.0.1', port='5432')
        self.cursor=self.conn.cursor()


    def csktm(self, ID, name, price, city):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cskteam (ID INT PRIMARY KEY NOT NULL, palyername VARCHAR(20) NOT NULL, price REAL, city CHAR(50))")
        postgres_insert_query = """ INSERT INTO allteams (ID, palyername,price, city) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (ID, name, price, city)
        self.cursor.execute(postgres_insert_query, record_to_insert)
        self.conn.commit()

    def tlo(self, ID, ps):
        record=""" SELECT * FROM allteam"""