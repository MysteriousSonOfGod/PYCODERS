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
cur.execute("create table Departments (Dept_id int(20) primary key not null, Dept_Name varchar(20) not null)")

c=cur.execute("show tables")
for i in cur:
    print(i)
mycon.close()




























