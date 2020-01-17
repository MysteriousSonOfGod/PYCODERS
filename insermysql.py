import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")
cur=myconn.cursor()
# sql="INSERT INTO customers (name,address, branch) values(%s, %s, %s)"
# val=["prasad","hyderabad", "CSE"]
# cur.execute(sql,val)
# myconn.commit()
cur.execute("SELECT * FROM customers")
r=cur.fetchall()
for i in r:
    print(i)

myconn.close()