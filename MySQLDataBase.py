# # import mysql.connector
# #
# # # Create the connection object
# # myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")
# #
# #
# # cur=myconn.cursor()
# # try:
# #   dbs=cur.execute("show tables")
# # except:
# #   myconn.rollback()
# #
# # for x in cur:
# #   print(x)
# # # printing the connection object
# # myconn.close()


# import mysql.connector

# mycon=mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")

# cur=mycon.cursor()


# try:
#     dbs=cur.execute("show databases")
#     # dt=cur.execute("show tables")
#     # print(dbs)
# except:
#     mycon.rollback()

# for i in cur:
#     print(i)

# # for j in cur:
# #     print(j)

import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="ravi")

cur=mycon.cursor()
# cur.execute("CREATE database PYTHONDB")
cur.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(20), address VARCHAR(200))")

c=cur.execute("desc customers")
for i in cur:
    print(i)
mycon.close()




























