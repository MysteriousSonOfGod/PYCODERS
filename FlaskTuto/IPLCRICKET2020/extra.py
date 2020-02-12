# # import sqlite3
# #
# # def readSqliteTable():
# #     try:
# #         sqliteConnection = sqlite3.connect('SQLite_Python.db')
# #         cursor = sqliteConnection.cursor()
# #         print("Connected to SQLite")
# #
# #         sqlite_select_query = """SELECT * from SqliteDb_developers"""
# #         cursor.execute(sqlite_select_query)
# #         records = cursor.fetchall()
# #         print("Total rows are:  ", len(records))
# #         print("Printing each row")
# #         for row in records:
# #             print("Id: ", row[0])
# #             print("Name: ", row[1])
# #             print("Email: ", row[2])
# #             print("JoiningDate: ", row[3])
# #             print("Salary: ", row[4])
# #             print("\n")
# #
# #         cursor.close()
# #
# #     except sqlite3.Error as error:
# #         print("Failed to read data from sqlite table", error)
# #     finally:
# #         if (sqliteConnection):
# #             sqliteConnection.close()
# #             print("The SQLite connection is closed")
# #
# # readSqliteTable()
#
#
# import sqlite3
#
# conn = sqlite3.connect('iplteams.db')
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE Emp
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print("Table created successfully")
#
# conn.close()
#
# #
# # import sqlite3
# #
# # conn = sqlite3.connect('iplteams.db')
# # print("Opened database successfully")
# #
# # conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) \
# # VALUES (1, 'Ajeet', 27, 'Delhi', 20000.00 )");
# #
# # conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) \
# # VALUES (2, 'Allen', 22, 'London', 25000.00 )");
# #
# # conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) \
# # VALUES (3, 'Mark', 29, 'CA', 200000.00 )");
# #
# # conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) \
# # VALUES (4, 'Kanchan', 22, 'Ghaziabad ', 65000.00 )");
# #
# # conn.commit()
# # print("Records inserted successfully"
# # )
#
#
# # !/usr/bin/python
#
# import sqlite3
#
# conn = sqlite3.connect('iplteams.db')
#
# data = conn.execute("select * from Employees");
#
# for row in data:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("ADDRESS = ", row[2])
#     print("SALARY = ", row[3], "\n")
#
# conn.close();

l=[('kal', 'Ravi'), ('kal', 'Ravi'), ('kal', 'Ravi'), ('CSK', 'csk123'), ('CSK', 'csk123'), ('CSK', 'csk123')]
# t=('kal', 'Ravi')
# print(type(t))
# for i in range(0, len(l)):
#     if l[i]==('C', 'csk123'):
#         print("YES")
#         break
name='CSK'
pa='csk123'
t=name, pa,
for i in range(0, len(l)):
    # import pdb
    # pdb.set_trace()
    if l[i]==t:
        print("YES")
        break
# tt=t, t
# print(tt)
# d=list(tt)
# print(d)

