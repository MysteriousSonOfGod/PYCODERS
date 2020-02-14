import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "Ravi@143",database = "ravi")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
  
    #Reading the Employee data      
    cur.execute("SELECT * FROM customers")  
  
    #fetching the rows from the cursor object  
    result = cur.fetchall()  
  
    for i in result:
        print(i)
except:  
    myconn.rollback()  
  
myconn.close()  