#-------------------------------------------pip install pymongo--------------------------------------------------------
import pymongo


#-------------------------------------------Staring Server-------------------------------------------------------------
#-------------------------------------------Mongo Default Port is 27017------------------------------------------------

uri="mongodb://127.0.0.1:27017"


client = pymongo.MongoClient(uri)

database = client['javatpoint']

collections = database['employees']

print(collections.find_one())