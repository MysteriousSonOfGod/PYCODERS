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
    cur.execute("UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'")
    mycon.commit()
    # for i in cur:
    #     print(i)
    con.execute("SELECT * FROM EMPLOYEE")
    # print("ASSENDING ORDER")
    # for j in con:
    #     print(j)
    for i in con:
        print(i)
except:
    mycon.rollback()
mycon.close()
