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
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database mysdb''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connecti