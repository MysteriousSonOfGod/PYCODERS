#ubuntu Login using Terminal
#sudo mysql -u root -p
#ENTER YOUR PASSWORD
import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143")
cur=mycon.cursor()
# cur.execute("use pydb")
cur.execute("show databases")
for i in cur:
    print(i)
mycon.close