import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='Ravi@143', host='127.0.0.1', database='ravi'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = '''SELECT * from EMPLOYEE INNER JOIN CONTACT ON EMPLOYEE.CONTACT = CONTACT.ID'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Closing the connection
conn.close()