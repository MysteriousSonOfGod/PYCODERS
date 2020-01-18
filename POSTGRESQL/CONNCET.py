#Ubuntu 18.04
#sudo -u postgres psql postgres or psql
#python -m pip install --upgrade pip
#pip install psycopg2
#(CHANGE PASSWORD) \password postgres
import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='Ravi@143', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()
