#ubuntu Login using Terminal
#sudo mysql -u root -p
#ENTER YOUR PASSWORD
import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="pydb")
cur=mycon.cursor()
# sql="INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s,%s,%s,%s,%s)"
# val=('Ramya', 'Ramapriya', 25, 'F', 5000)
try:
    cur.execute(" SELECT * FROM EMPLOYEE WHERE INCOME > 4000;")
    for i in cur:
        print(i)
except:
    mycon.rollback()
mycon.close()
