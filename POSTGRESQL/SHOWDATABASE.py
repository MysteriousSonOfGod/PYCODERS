import psycopg2
mycon=psycopg2.connect(database="pydb", user="postgres", password="Ravi@143", host="127.0.0.1", port="5432")
cur=mycon.cursor()
sql="\l"
cur.execute(sql)
for i in cur:
    print(i)
mycon.close()