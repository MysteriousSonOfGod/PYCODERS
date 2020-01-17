import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")
cur=myconn.cursor()
try:
    # cur.execute("alter table customers add branch VARCHAR(20) not null")
    cur.execute("desc customers")
except:
    myconn.rollback()

for i in cur:
    print(i)

myconn.close()