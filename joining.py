import mysql.connector
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")
cur=myconn.cursor()
# sql="INSERT INTO Departments (Dept_id,Dept_Name) values(%s, %s)"
# val=[21,"IT"]

# cur.execute(sql,val)
# myconn.commit()
# cur.execute("SELECT * FROM Departments")
# r=cur.fetchall()
# for i in r:
#     print(i)

cur.execute("SELECT customers.name, customers.address, customers.branch, Departments.Dept_id, Departments.Dept_Name FROM Departments join customers Departments")
print("ID    Name    Salary    Dept_Id    Dept_Name")  
for row in cur:  
        print("%d    %s    %d    %d    %s"%(row[0], row[1],row[2],row[3],row[4]))  
myconn.close()


#REFERENCE
#https://www.tutorialspoint.com/python_data_access/python_mysql_join.htm