#-----------------------------------------------pip install pymongo--------------------------------------------------
from pymongo import MongoClient
#----------------------------------------------mongoDB port Number 2707-----------------------------------------------
cli = MongoClient('localhost', 27017)
#----------------------------------------------Connect To DataBase----------------------------------------------------
conn = cli['mydb']
#----------------------------------------------Find Number Of Mongo Databases-------------------------------------------
show = cli.database_names()
print(show)
# create=cli.createCollection("SSSIT")