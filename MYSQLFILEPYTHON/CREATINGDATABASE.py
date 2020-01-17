#ubuntu Login using Terminal
#sudo mysql -u root -p
#ENTER YOUR PASSWORD
import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")
cur=mycon.cursor()
# cur.execute("CREATE database pydb")
mycon.close