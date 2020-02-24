#-------------------------------------------pip install pymongo--------------------------------------------------------

from pymongo import MongoClient

#-------------------------------------------Creating a pymongo client---------------------------------------------------
client = MongoClient('localhost', 27017)

#-------------------------------------------Getting the database instance-----------------------------------------------
db = client['mydb']
print("Database created........")

#-------------------------------------------Verification----------------------------------------------------------------
print("List of databases after creating new one")
print(client.list_database_names())


# #-------------------------------------------pip install pymongo--------------------------------------------------------
# import pymongo
#
#
# #-------------------------------------------Staring Server-------------------------------------------------------------
# #-------------------------------------------Mongo Default Port is 27017------------------------------------------------
#
# uri="mongodb://127.0.0.1:27017"
#
#
# client = pymongo.MongoClient(uri)
#
# database = client['javatpoint']
#
# collections = database['employees']
#
# print(collections.find_one())