import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")
cur=myconn.cursor()
# sql="INSERT INTO Departments (Dept_id,Dept_Name) values(%s, %s)"
# val=[21,"IT"]

# cur.execute(sql,val)
# myconn.commit()
cur.execute("SELECT * FROM customers")
r=cur.fetchall()
for i in r:
    print(i)

myconn.close()