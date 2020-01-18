#ubuntu Login using Terminal
#sudo mysql -u root -p
#ENTER YOUR PASSWORD
import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="pydb")
cur=mycon.cursor()
con=mycon.cursor()
# sql="INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s,%s,%s,%s,%s)"
# val=('Ramya', 'Ramapriya', 25, 'F', 5000)
try:
    print("DESENDING ORDER")
    cur.execute(" SELECT * FROM EMPLOYEE ORDER BY FIRST_NAME, INCOME DESC;")
    for i in cur:
        print(i)
    con.execute("SELECT * FROM EMPLOYEE ORDER BY AGE;")
    print("ASSENDING ORDER")
    for j in con:
        print(j)
except:
    mycon.rollback()
mycon.close()
