import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="pydb", user='postgres', password='Ravi@143', host='127.0.0.1', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * FROM CRICKETERS;''')

#Fetching 1st row from the table
# result = cursor.fetchone();
# print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
for i in result:
    print(i)
#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()